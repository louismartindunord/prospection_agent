import sqlite3

# à modifier pour mieux s'adapter à mes besoins 
# documentation https://python.langchain.com/docs/integrations/vectorstores/sqlitevec/
class UserVectorstore:

    def __init__(self, db_path="vector_store.db", embedding_size=1536):
        self.db_path = db_path
        self.embedding_size = embedding_size
        self.conn = sqlite3.connect(self.db_path)
        self.conn.enable_load_extension(True)
        self.conn.execute("SELECT load_extension('vss0')")
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        self.conn.execute(f"""
            CREATE VIRTUAL TABLE IF NOT EXISTS document_index
            USING vss(content_embedding({self.embedding_size}));
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS document_metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                document_id INTEGER,
                content TEXT,
                FOREIGN KEY(document_id) REFERENCES document_index(rowid)
            );
        """)
        self.conn.commit()

    def insert_document(self, user_id: int, embedding: list[float], content: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO document_index (content_embedding) VALUES (?)",
            (embedding,)
        )
        doc_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO document_metadata (user_id, document_id, content) VALUES (?, ?, ?)",
            (user_id, doc_id, content)
        )
        self.conn.commit()
        return doc_id

    def search(self, user_id: int, query_embedding: list[float], k=5):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT m.content, m.user_id, m.id, vss_distance(v.content_embedding, ?) AS score
            FROM document_index v
            JOIN document_metadata m ON v.rowid = m.document_id
            WHERE m.user_id = ?
            ORDER BY vss_search(v.content_embedding, ?)
            LIMIT ?;
        """, (query_embedding, user_id, query_embedding, k))

        return [dict(row) for row in cursor.fetchall()]

    def close(self):
        self.conn.close()
        
        
        
#exemple d'utilisation dans un autre fichier 
store = VectorStoreManager()

# ⚠️ Exemple de vecteur fictif
dummy_embedding = [0.01] * 1536
user_id = 1

store.insert_document(user_id, dummy_embedding, "Voici un document pour l'utilisateur 1")
results = store.search(user_id, dummy_embedding, k=3)

for r in results:
    print(r["score"], r["content"])

store.close()