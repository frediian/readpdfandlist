import pandas as pd
import sys

archiveExcel= "./excel/"+str(sys.argv[1])+".xls"

datos = pd.read_excel(archiveExcel, dtype='str',index_col=None)

col_id = "NÚMERO IDENTIFICACIÓN"
col_name = "NOMBRES"

person_id= str(sys.argv[2])
info = datos[datos[col_id]==person_id][col_name]

if info.empty:
    print("Not found")
else:
    print(info.values[0])