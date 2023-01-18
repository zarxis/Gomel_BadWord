import sqlite3 as sql

con = sql.connect('path_to_db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `test` (id INTEGER64)")
    con.commit
    cur.close()
cur.close()