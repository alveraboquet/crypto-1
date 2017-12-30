import pandas as pd
import multiprocessing as mp
from api import Bittrex
import sqlite3 as sl
from time import time
import sys

BITTREX_MARKETS_FILE = './metadata/bittrex_markets.csv'
DB_PATH = './cryptodata.db'
bittrex = Bittrex()

def post_to_db(values,time):
    conn = sl.connect(DB_PATH)
    cursor = conn.cursor()
    for value in values:
        insert_query = ('INSERT INTO prices (MARKET,PRICE,TIMESTAMP) VALUES (' + ','.join(['"'+str(value[0])+'"',str(value[1]),'"'+time+'"']) + ')')
        cursor.execute(insert_query)
    conn.commit()
    conn.close()

def sample_wrapper(time):
    market_metadata = pd.read_csv(BITTREX_MARKETS_FILE)
    markets = list(market_metadata['MarketName'])
    pool = mp.Pool(processes = 8)
    result = pool.map(sample, markets)
    post_to_db(result,time)

def sample(market_name):
    px = bittrex.get_current_fair_px({'market' : market_name})
    return (market_name, px)

def main(args):
    time = ' '.join(args[1:3])
    time = time[:-2] + '00'
    sample_wrapper(time) 

if __name__ == '__main__':
    main(sys.argv)
