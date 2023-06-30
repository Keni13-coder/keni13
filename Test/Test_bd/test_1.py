import pymysql
from config import *
def create_connection_1(host_name, user_name, user_password,database=None ):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("Connection to MySQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection_1(host, user, password,bd_name)
def sel(connection):
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM хуй')
    # print(cursor.fetchall())
    print(connection.cursor().execute('SELECT * FROM хуй'))
    
# sel(connection)    

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")
        
def dell(connection):
    connection.cursor().execute('DELETE FROM хуй')
    connection.commit()


# dell(connection)           