
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',           # Change this to your MySQL host
            database='',   # Change this to your database name
            user='root',       # Change this to your MySQL username
            password='asr'    # Change this to your MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if cursor.with_rows:
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            connection.commit()
            print(f"Query executed successfully. Rows affected: {cursor.rowcount}")
    except Error as e:
        print(f"Error executing query: {e}")

def main():
    connection = connect_to_database()
    if connection:
        while True:
            print("\nMySQL Query Tool")
            print("1. Execute Query")
            print("2. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                query = input("Enter your SQL query: ")
                execute_query(connection, query)
                
            elif choice == '2':
                connection.close()
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
