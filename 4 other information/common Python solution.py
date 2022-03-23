'''1. get the file's path, which is in the current working directory'''
import os
workpath = os.getcwd()   # get the current work directory
for root, dirs, files in os.walk(workpath):
    for name in files:
        if name == 'testdata.xlsx':   #the specific file is testdata.xlsx
            print(os.path.abspath(os.path.join(root, name)))

'''2. get the current py file's filepath'''
print(os.path.dirname(os.path.abspath(__file__)))

'''3. go through all files in the given directory'''
for file in os.listdir(workpath):
    filename = os.fsdecode(file)
    print(os.path.join(workpath, filename))


'''4. flatten tuple in tuples/ get all the elements of tuple in tuples
https://stackoverflow.com/questions/10632839/transform-list-of-tuples-into-a-flat-list-or-a-matrix
'''
list1 = [('Ford', 'tesla'), ('aFord', 'btesla')]
flatten_list1 = list(sum(l1, ()))
print(flatten_list1)
# improvemnt trainning : flaten the tuple in tuples, which in list
list2 = [(('Ford', 'tesla'), ('aFord', 'btesla')), (('Mustang', 'Mustang'), ('Mustang', 'Mustang')),((1964, 2012), (1964, 2012))]
flatten_list2 = [list(sum(item, ())) for item in list2]
print(flatten_list2)

'''4.1 flatten the most insde list
[[['Ford', 'tesla'], ['Mustang', 'Mustang'], [1964, 2012]], [['aFord', 'btesla'], ['Mustang', 'Mustang'], [1964, 2012]]]
[['Ford', 'tesla', 'aFord', 'btesla'], ['Mustang', 'Mustang', 'Mustang', 'Mustang'],['1964', '2012', '1964', '2012']]
'''
import numpy as np 
lis1 = [[['Ford', 'tesla'], ['Mustang', 'Mustang'], [1964, 2012]], [['aFord', 'btesla'], ['Mustang', 'Mustang'], [1964, 2012]]]
lis2 = list(zip(*alldata_values))  # [(['Ford', 'tesla'], ['aFord', 'btesla']), (['Mustang', 'Mustang'], ['Mustang', 'Mustang']), ([1964, 2012], [1964, 2012])]
a = np.array(lis2).reshape(-1,4)
print(a)

'''5. covert dataframe into dictionary with index'''
car= {'brand': ('aFord', 'btesla'),
 'model': ('Mustang', 'Mustang'),
 'year': (1964, 2012)}
dd1 = pd.DataFrame(car)
dd2 = dd1.to_dict()
dd3 = dd1.to_dict('list')

'''6. 3D list, covert the most inside part into tuple
[[['Ford', 'tesla'], ['Mustang', 'Mustang'], [1964, 2012]], [['aFord', 'btesla'], ['Mustang', 'Mustang'], [1964, 2012]]]
[[('Ford', 'Mustang', 1964), ('tesla', 'Mustang', 2012)], [('aFord', 'Mustang', 1964), ('btesla', 'Mustang', 2012)]]
'''
lis1 = [[['Ford', 'tesla'], ['Mustang', 'Mustang'], [1964, 2012]], [['aFord', 'btesla'], ['Mustang', 'Mustang'], [1964, 2012]]]
print([list(zip(*item)) for item in lis1])


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