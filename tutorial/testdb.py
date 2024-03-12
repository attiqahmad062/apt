import mysql.connector

# MySQL database settings
MYSQL_SETTINGS = {
    'host': 'localhost',
    'port': 3306,
    'database': 'etiapt',
    'user': 'root',
    'password': '7777',
}

def main():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(**MYSQL_SETTINGS)
        if conn.is_connected():
            print("Connected to MySQL database")

        # Perform database operations here...

        # Close connection
        conn.close()
        print("Connection closed")
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)

if __name__ == "__main__":
    main()
