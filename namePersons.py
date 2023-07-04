import pandas as pd
import sys

archiveExcel= "./excel/"+str(sys.argv[1])+".xls"

datos = pd.read_excel(archiveExcel, dtype='str',index_col=None)

col_id = "NÚMERO IDENTIFICACIÓN"
col_name = "NOMBRES"

person_id= str(sys.argv[2])

print(datos[datos[col_id]==person_id][col_name].values[0])