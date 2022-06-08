from importlib.machinery import PathFinder
import pandas as pd
import numpy as np

path = r'C:\Users\Staff\OneDrive - University of Huddersfield\Documents\002 data project\007 course progression\data report\20211028 Progression Tables - HHS.xlsx'
xls_file = pd.ExcelFile(path)
# print(xls_file.sheet_names)
for sheetname in xls_file.sheet_names:
    df_new = pd.DataFrame()
    print(sheetname)  # 1. student characteristics

    df = pd.read_excel(path,sheet_name=sheetname)
    start_num = df.loc[df.iloc[:,0]=='School'].index.tolist()[0]    #get the row index of data starts

    # print(df.iloc[start_num+1:,0:5].to_string(header=False))    #get the course details

    acy = df.iloc[start_num-2,5]
    df_new['year']= acy
    
    df_new['gap'] = df.iloc[start_num+1:,6]-df.iloc[start_num+1:,8]
    print(df_new)

    # print(df.iloc[start_num:,6]-df.iloc[start_num:,7])
    break
    
# print(df)
