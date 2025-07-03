import sqlite3
from datetime import datetime


class LoginHistoryModel:
    def __init__(self, db_path="data/face-recognition-db.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_login_table()

    def _create_login_table(self):
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS login_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uid TEXT,
            fname TEXT,
            lname TEXT,
            date TEXT,
            time TEXT
        )
        """)
        self.conn.commit()

    def add_login_entry(self, uid, fname, lname):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        cur = self.conn.cursor()
        cur.execute("""
        INSERT INTO login_history (uid, fname, lname, date, time)
        VALUES (?, ?, ?, ?, ?)
        """, (uid, fname, lname, date_str, time_str))
        self.conn.commit()

    def get_all_entries(self):
        cur = self.conn.cursor()
        return cur.execute("SELECT uid, fname, lname, date, time FROM login_history ORDER BY id DESC").fetchall()
    
    def clear_login_history(self):
        cursor = self.conn.cursor()
        
        # Delete all records
        cursor.execute(f"DELETE FROM user_table;")
        
        # Reset auto-increment counter (if table has INTEGER PRIMARY KEY)
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='user_table';")
        
        # Compact database
        cursor.execute("VACUUM;")
        
        self.conn.commit()
        self.conn.close()
