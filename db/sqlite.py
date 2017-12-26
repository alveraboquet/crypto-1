
import sqlite3

class Sqlite(object):

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def create_table(
