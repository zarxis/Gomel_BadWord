import sqlite3

con = sqlite3.connect('path_to_db', check_same_thread=False)
cur = con.cursor()

def db_table_val(user_id: int, first_name: str, last_name: str,):
	cur.execute('INSERT INTO BadWord(user_id, first_name, last_name) VALUES (?, ?, ?)', (user_id, first_name, last_name))
	con.commit()
