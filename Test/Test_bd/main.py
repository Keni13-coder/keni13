import pymysql
from config import *

try:
    
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database='mybd'

        # cursorclass=pymysql.cursors.DictCursor
        )
    mycursor = connection.cursor()

    # mycursor.execute('CREATE TABLE хуй(FGFGG TEXT);')
    # mycursor.execute('ALTER TABLE хуй  ADD id int PRIMARY KEY AUTO_INCREMENT  FIRST')
    mycursor.execute('INSERT INTO хуй (id , FGFGG) VALUES (%s,%s)',(3,"2"))
    connection.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)
    
    

except Exception as ex:
    print('Дерьмо')
    print(ex)    
