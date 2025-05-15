import sqlite3


def create_empty_sqlite_database():
    try : 
        with sqlite3.connect("database.db") as conn:
            print(f"création de la base de données avec la version {sqlite3.sqlite_version}")
    except sqlite3.OperationalError as error: 
        print(f"Error : {error}")
        
def create_connection(): 
    try : 
        conn =  sqlite3.connect("database.db")
        return conn
    except sqlite3.OperationalError as error:
       print(f"impossible de se connecter à la base de donnée  erreur {error}") 
    
    
    
def modify_database():
    conn = create_connection()
    cursor = conn.cursor()
    try : 
        with open("sql/database_gestion.sql", "r") as f:
            sql = f.read()
            cursor.executescript(sql,)
            print("tables modifiée avec succés")
    except sqlite3.OperationalError as error :
        print(f"Probleme lors de la manipulation de la table {error}")
    finally:
        cursor.close()
        conn.close()
        
    
        
        
if __name__ == "__main__":
    modify_database()
    
    