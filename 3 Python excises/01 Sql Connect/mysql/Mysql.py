import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# read testdata into dataframe
for root, dirs, files in os.walk(os.getcwd()):
    for name in files:
        if name == 'testdata.xlsx':   #the specific file is testdata.xlsx
            datapath = os.path.abspath(os.path.join(root, name))

testdata = pd.read_excel(datapath)

# connect to the database
connection = pymysql.connect(host='localhost',
                         user='root',
                         password="123456",
                         db='mevaluation',
                         charset='utf8mb4')

#create cursor
mycursor=connection.cursor()

# create engine 
db_data = 'mysql+pymysql://' + 'root' + ':' + '123456' + '@' + 'localhost' + ':3306/' \
       + 'mevaluation' + '?charset=utf8mb4'
engine = create_engine(db_data)

'''way 1 : import dataframe into mysql database'''
mycursor.execute("drop TABLE users;")
testdata.to_sql('users', con=engine, index=False)

'''way 2 : insert dataframe into the existed table (fastest)'''
mycursor.execute("drop TABLE testdata;")
mycursor.execute("CREATE TABLE testdata (id int PRIMARY KEY, name VARCHAR(255), runtime TIMESTAMP)")
testdata.to_sql('testdata', engine, if_exists='append', index=False)   

'''way 3 : Insert DataFrame records one by one'''
cols = ",".join([str(i) for i in testdata.columns.tolist()])
for i,row in testdata.iterrows():
    sql = "INSERT INTO users (" +cols + ") VALUES (" + "%s,"*(len(row)-1) + "%s)"
    mycursor.execute(sql, tuple(row))
    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()

# Fetch all the records
mycursor.execute('select * from testdata')
result = mycursor.fetchall()
for i in result:
    print(i)

engine.dispose()
connection.close()