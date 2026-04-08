import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3306",
            database="expense_manager_db"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def fetch_all(self, query, values=None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()


    def add_user(self, name):
        query = "INSERT INTO users (name) VALUES (%s)"
        return self.execute_query(query, (name,))
    
    def get_expenses(self, user_id):
        query = """
        SELECT u.name, e.*
        FROM expenses e
        JOIN users u ON e.user_id = u.user_id
        WHERE e.user_id = %s
        """
        return self.fetch_all(query, (user_id,))