import pandas as pd
import sys


archiveExcel= "./excel/"+str(sys.argv[1])+".xls"

datos = pd.read_excel(archiveExcel, dtype='str')

#print((datos.columns))
find_data = "NÚMERO IDENTIFICACIÓN"
persons=datos.get(find_data)
numero=1085
ced='1900855634'
print(numero in datos[find_data])
print(ced in datos[find_data].values)
print(datos[find_data].keys())
print( datos[find_data][numero])