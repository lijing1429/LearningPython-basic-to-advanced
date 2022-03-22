'''1. get the file's path, which is in the current working directory'''
import os
workpath = os.getcwd()   # get the current work directory
for root, dirs, files in os.walk(workpath):
    for name in files:
        if name == 'testdata.xlsx':   #the specific file is testdata.xlsx
            print(os.path.abspath(os.path.join(root, name)))

'''2. write sql : insert dataframe records one by one'''
import pandas as pd
df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8],
                   'specimen': ['falcon', 'dog', 'spider', 'fish']}
                   )

cols = ",".join([str(i) for i in df.columns.tolist()]) # get dataframe' column name

for i, row in df.iterrows():
    sql = "INSERT INTO users (" + cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"
    print(sql, tuple(row))