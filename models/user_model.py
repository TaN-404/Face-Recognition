import sqlite3
import pickle
import os


class UserModel:
    def __init__(self, db_path="data/attendance.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_user_table()

    def _create_user_table(self):
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS user_table (
            uid TEXT PRIMARY KEY,
            fname TEXT,
            lname TEXT,
            image1_path TEXT,
            image2_path TEXT,
            image3_path TEXT,
            embedding1 BLOB,
            embedding2 BLOB,
            embedding3 BLOB,
            avg_embedding BLOB
        )
        """)
        self.conn.commit()

    def save_user(self, uid, fname, lname, image_paths, embeddings, avg_embedding):
        cur = self.conn.cursor()
        cur.execute("""
        INSERT INTO user_table (uid, fname, lname, image1_path, image2_path, image3_path,
                                embedding1, embedding2, embedding3, avg_embedding)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            uid, fname, lname,
            image_paths[0], image_paths[1], image_paths[2],
            pickle.dumps(embeddings[0]),
            pickle.dumps(embeddings[1]),
            pickle.dumps(embeddings[2]),
            pickle.dumps(avg_embedding)
        ))
        self.conn.commit()

    def get_all_users(self):
        cur = self.conn.cursor()
        return cur.execute("SELECT uid, fname, lname FROM user_table").fetchall()

    def get_user_embedding(self, uid):
        cur = self.conn.cursor()
        row = cur.execute("SELECT avg_embedding FROM user_table WHERE uid=?", (uid,)).fetchone()
        return pickle.loads(row[0]) if row else None
    


    def get_all_avg_embeddings(self): 
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT avg_embedding FROM user_table")
        
        embeddings_list = []

        for row in cursor.fetchall():
            pickled_data = row[0]
            
            if pickled_data is not None:
                try:
                    embedding = pickle.loads(pickled_data)
                    embeddings_list.append(embedding)
                except Exception as e:
                    print(f"Error unpickling embedding: {e}")
        
        self.conn.close()
        return embeddings_list
