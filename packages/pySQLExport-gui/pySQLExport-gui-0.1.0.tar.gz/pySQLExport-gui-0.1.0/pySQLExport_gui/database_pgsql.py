# database_pgsql.py
import psycopg2

class PgSQLDatabase:
    def __init__(self, host, user, password, database, port):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=database,
            port=port
        )
    
    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        return results, columns
    
    def close(self):
        if self.connection:
            self.connection.close()