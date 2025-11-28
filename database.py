import sqlite3
from pathlib import Path

DB_NAME = "produtos.db"

def get_connection():
    db_path = Path(DB_NAME)
    conn = sqlite3.connect(db_path) # conexao
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS produtos
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
        )"""
    )
    conn.commit()
    conn.close()




if __name__ == "__main__":
    create_table()
    