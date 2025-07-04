import sqlite3
import pickle
import os
import numpy as np
from datetime import datetime
import shutil


class UserModel:
    def __init__(self, db_path="data/face-recognition-db.db"):
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
            avg_embedding BLOB,
            date TEXT,
            time TEXT
        )
        """)
        self.conn.commit()

    def save_user(self, uid, fname, lname, image_paths, embeddings, avg_embedding):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        cur = self.conn.cursor()
        cur.execute("""
        INSERT INTO user_table (uid, fname, lname, image1_path, image2_path, image3_path,
                                embedding1, embedding2, embedding3, avg_embedding, date, time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            uid, fname, lname,
            image_paths[0], image_paths[1], image_paths[2],
            pickle.dumps(embeddings[0]),
            pickle.dumps(embeddings[1]),
            pickle.dumps(embeddings[2]),
            pickle.dumps(avg_embedding),
            date_str,
            time_str
        ))
        self.conn.commit()

    def get_all_users(self):
        cur = self.conn.cursor()
        return cur.execute("SELECT uid, fname, lname, date, time FROM user_table").fetchall()

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
        
        return embeddings_list
    

    def drop_user_table(self):
        cursor = self.conn.cursor()
        
        # Delete all records
        cursor.execute(f"DELETE FROM user_table;")
        
        # Reset auto-increment counter (if table has INTEGER PRIMARY KEY)
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='user_table';")

        folder_name = "data/images"
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            shutil.rmtree(folder_name)
            print(f"Folder '{folder_name}' deleted.")
        
        self.conn.commit()

    def get_user_from_embedding(self, target_embedding):

        try:
            print("step 1")
            cursor = self.conn.cursor()
            
            # Search through all embeddings
            cursor.execute("SELECT uid, fname, lname, avg_embedding FROM user_table")
            
            for row in cursor.fetchall():
                uid, fname, lname, pickled_embed = row
                try:
                    print("step 2")
                    # Unpickle the stored embedding
                    stored_embed = pickle.loads(pickled_embed)
                    print(stored_embed)
                    
                    # Compare embeddings (using numpy for example)
                    if np.array_equal(stored_embed, target_embedding):
                        return {
                            'uid': uid,
                            'fname': fname,
                            'lname': lname,
                            'match': True
                        }
                        
                except pickle.UnpicklingError:
                    continue
                    
            return None
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None


    def get_username_from_embedding(self, target_embedding):

        try:
            ("step 1")
            cursor = self.conn.cursor()
            
            # Search through all embeddings
            cursor.execute("SELECT uid, fname, lname, avg_embedding FROM user_table")
            
            for row in cursor.fetchall():
                uid, fname, lname, pickled_embed = row
                try:
                    ("step 2")
                    # Unpickle the stored embedding
                    stored_embed = pickle.loads(pickled_embed)
                    
                    # Compare embeddings (using numpy for example)
                    if np.array_equal(stored_embed, target_embedding):
                        full_name = f"{fname} {lname}" 
                        return full_name, uid,fname, lname
                        
                except pickle.UnpicklingError:
                    continue
                    
            return None
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None


    def search_by_uid(self, uid):
        cur = self.conn.cursor()
        cur.execute("SELECT uid, fname, lname FROM user_table WHERE uid LIKE ?", (f"%{uid}%",))
        return [{'uid': row[0], 'fname': row[1], 'lname': row[2]} for row in cur.fetchall()]

    def search_by_fname(self, fname):
        cur = self.conn.cursor()
        cur.execute("SELECT uid, fname, lname FROM user_table WHERE fname LIKE ?", (f"%{fname}%",))
        return [{'uid': row[0], 'fname': row[1], 'lname': row[2]} for row in cur.fetchall()]

    def search_by_lname(self, lname):
        cur = self.conn.cursor()
        cur.execute("SELECT uid, fname, lname FROM user_table WHERE lname LIKE ?", (f"%{lname}%",))
        return [{'uid': row[0], 'fname': row[1], 'lname': row[2]} for row in cur.fetchall()]

    def search_all_fields(self, text):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT uid, fname, lname FROM user_table 
            WHERE uid LIKE ? OR fname LIKE ? OR lname LIKE ?
        """, (f"%{text}%", f"%{text}%", f"%{text}%"))
        return [{'uid': row[0], 'fname': row[1], 'lname': row[2]} for row in cur.fetchall()]

    def delete_user(self, uid):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM user_table WHERE uid = ?", (uid,))
            self.conn.commit()
            path = "data/images"
            folder_name = f"{path}/{uid}"
            if os.path.exists(folder_name) and os.path.isdir(folder_name):
                shutil.rmtree(folder_name)
                print(f"Folder '{folder_name}' deleted.")
            return cur.rowcount > 0
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def update_user(self, uid, fname, lname):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE user_table 
                SET fname = ?, lname = ? 
                WHERE uid = ?
            """, (fname, lname, uid))
            self.conn.commit()
            return cur.rowcount > 0
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

            