import pandas as pd

path = r'C:\Users\SHUMJL7\OneDrive - University of Huddersfield\Documents\002 data project\007 course progression\data report\age.xlsx'

Sexdata = pd.read_excel(path,sheet_name= 'sex')

print(Sexdata)

# add new rows - 'gap' according to different sex type: KPI attainment of gap = male - female (same year, same course and same route)
