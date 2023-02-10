import sqlite3

con = sqlite3.connect('path_to_db.db', check_same_thread=False)
cur = con.cursor()

class db_CON:
    def INSERT(user_id: int, first_name: str, last_name: str, stat: int):
        cur.execute('INSERT INTO BadWord(user_id, first_name, last_name, stat) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, stat))
        con.commit()
        con.close()
        cur.close()
        
    def UPDATE(stat: int, user_id):
        cur.execute('UPDATE BadWord SET stat = ? WHERE user_id = ?', (user_id, stat))
        con.commit()
        con.close()
        cur.close()
