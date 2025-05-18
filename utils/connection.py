import sqlite3


def create_connection():
    try:
        conn = sqlite3.connect("prospection.db")
        return conn
    except sqlite3.OperationalError as error:
        print(f"impossible de se connecter à la base de donnée  erreur {error}")
