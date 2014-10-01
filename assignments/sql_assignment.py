from lib.postgres_db import MyDB
import pandas as pd
import json

class TripleCrownSql(object):
  def __init__(self):
    with open('./database.json', 'r') as f:
      db_config = json.load(f)

    self.db = MyDB(**db_config)
    self.conn = self.db._db_connection

  def setup_triple_crown_table(self):
    self.db.execute('''
        create temp table triple_crown_winners as
        select * from awardsplayers
        where awardid like '%Triple Crown%';
    ''')

  def get_triple_crown_table(self):
    self.setup_triple_crown_table()
    sql = "select * from triple_crown_winners"
    return pd.io.sql.read_sql(sql, self.conn)

df = TripleCrownSql().get_triple_crown_table()

