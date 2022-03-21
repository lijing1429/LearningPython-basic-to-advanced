import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
  # ,database="mevaluation"
)

mycursor = mydb.cursor()
'''1. show your database / tables in your local devices'''
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

'''2. create table in your database'''
# mycursor.execute("CREATE TABLE mevaluation.test (name VARCHAR(255) PRIMARY KEY, address VARCHAR(255))")

'''3. insert data into table (use "commit" at the end of statement, otherwise the values won't insert)'''
# mycursor.execute("INSERT INTO mevaluation.module_result VALUES(%s, %s, %s)", ("testpy", "789465485",int(90)))

# sql = "INSERT INTO mevaluation.module_result (SPRcode,candidaNumber,studentMarks) VALUES (%s, %s, %s)"
# val = ('testpy1', '789465485',90)
# mycursor.execute(sql, val)

# mydb.commit()

'''4. manipulate table in your database'''

# mycursor.execute("insert into mevaluation.module_result (SPRcode,candidaNumber,studentMarks) values ('123458', '789465485',80)")
# mydb.commit()