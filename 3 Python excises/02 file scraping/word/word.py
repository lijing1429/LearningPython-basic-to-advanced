'''This py aims to scrap table from test.docx. 
If you want to learn how does it work, just download word folder and run the py file.'''

import os
import pandas as pd
from docx import Document
import docx2txt
import re

'''1. get the word file path'''
workpath = os.getcwd()   # get the current work directory
for root, dirs, files in os.walk(workpath):
    for name in files:
        if name == 'test.docx':   #the specific file is testdata.xlsx
            filepath = os.path.abspath(os.path.join(root, name))
print(filepath)

'''2. scrapy data from word'''
mytext = docx2txt.process(filepath)
parts = re.split('[\n|\t]\d{1,2}\.[\n|\t]', mytext)
getext = parts[0].split('\n\n')[1:]
print(getext)

'''3. insert data into dataframe'''
numes = [index for index, value in enumerate(getext) if value.isdigit()]
columnname = getext[0,numes[0]]
print(numes)
print(columnname)


# m_key = []
# m_value = []
# for ws in parts[0]:
#     numb = ws.find('\n\n')
#     m_key.append(ws[0:numb])
#     m_value.append(ws[numb:].lstrip('\n|\t| '))

# output_excel = pd.DataFrame([m_value],columns =m_key )
# print(output_excel)
