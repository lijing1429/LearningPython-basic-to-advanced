import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)

mycursor = mydb.cursor()
'''1. show your database in your local devices'''
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

'''2. create table in your database'''
mycursor.execute('''CREATE TABLE customers 
                  (id INT AUTO_INCREMENT PRIMARY KEY, 
                    name VARCHAR(255), address VARCHAR(255))''')