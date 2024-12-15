import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "secret",
            database = "carhopper",
            port = 3334
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None