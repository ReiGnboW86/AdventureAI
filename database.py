import psycopg2

class Database:
    def __init__(self, dbname, user, password, host='localhost'):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        self.cursor = self.connection.cursor()

    def store_memory(self, key, value):
        self.cursor.execute("INSERT INTO memories (key, value) VALUES (%s, %s)", (key, value))
        self.connection.commit()

    def retrieve_memory(self, key):
        self.cursor.execute("SELECT value FROM memories WHERE key = %s", (key,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
