import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

def recreate_users_table(conn):
    try:
        cursor = conn.cursor()
        
        cursor.execute("DROP TABLE IF EXISTS users")
        
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE
            )
        ''')
        
    except sqlite3.Error as e:
        print(f"Error: {e}")

def create_high_scores_table(conn):
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS high_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                high_score INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
    except sqlite3.Error as e:
        print(f"Error: {e}")

def main():
    database = "questions.db"  
    
    conn = create_connection(database)
    
    if conn is not None:
        recreate_users_table(conn)
        
        create_high_scores_table(conn)
        
        conn.close()
    else:
        print("ERROR")

if __name__ == '__main__':
    main()
