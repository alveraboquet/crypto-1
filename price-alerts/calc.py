
import sqlite3 as sl
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import multiprocessing as mp
from sample import get_markets
import sys

DB_PATH = './cryptodata.db'

def get_data():
    conn = sl.connect(DB_PATH)
    select_query = 'SELECT * FROM prices';
    df = pd.io.sql.read_sql(select_query, conn)
#    if start_date:
#        select_query += ' WHERE TIMESTAMP >= %s' % start_date
#    if end_date:
#	select_query += ' AND WHERE TIMESTAMP <= %s' % end_date
    conn.close()
    return df

def update_changes(time):
    df = get_data().sort_values('TIMESTAMP')
    markets = get_markets()
    # 5, 10, 20, 30, 60, 120, 180, 360, 720, 1440,2,3,4,5,6,7
    c = {}
    for mkt in markets:
        mkt_data = df.query('MARKET=="%s"' % mkt).reset_index()
	size = mkt_data.shape[0]
        curr_price = mkt_data.ix[size-1]['PRICE']
        curr_time = mkt_data.ix[size-1]['TIMESTAMP']
	curr_dt = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        changes = []
        for delta in [5,10,20,30,60,120,180,360,720,1440,2*1440,3*1440,4*1440,5*1440,6*1440,7*1440]:
            past_dt = curr_dt - timedelta(minutes=delta)
	    past_time = past_dt.strftime('%Y-%m-%d %H:%M:%S')
	    past_price = mkt_data.query('TIMESTAMP=="%s"' % past_time)
	    if not past_price.empty:
	        changes.append((delta, (curr_price - past_price) / past_price))
	    else:
		changes.append((delta, np.nan))
        c[mkt] = changes
    return c

def main(args):
#    time = ' '.join(args[1:3])
#    update_changes(time)
    pass

print update_changes('2017-12-30 01:10:00')

if __name__ == '__main__':
    main(sys.argv)
