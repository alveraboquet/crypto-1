
import sqlite3

class Sqlite(object):

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def insert(self, table_name, columns, values):
        num_items = len(values)
	values = columns + [table_name] + values
        flags = '('+'%s,'*(num_items-1)+'%s'+')'
        insert_query = ('INSERT INTO %s ' + flags + ' VALUES ' + flags) % tuple(values)
	print insert_query
'''
	cursor = self.conn.cursor()
        cursor.execute(insert_query)
	self.conn.commit()
   ''' 
