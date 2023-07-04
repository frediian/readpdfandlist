import pandas as pd
import sys


archiveExcel= "./excel/"+str(sys.argv[1])+".xls"

datos = pd.read_excel(archiveExcel, dtype='str',index_col=None)

#print((datos.columns))
find_data = "NÚMERO IDENTIFICACIÓN"
find_name = "NOMBRES"

persons=datos.get(find_data)
numero=1085
ced='1900855634'
df = pd.DataFrame(data=datos[find_name], index=datos[find_data])
#df.set_index([find_data, find_name])
print(df.index)

print(df[find_name].get(ced))
#print(numero in datos[find_data])
#print(ced in datos[find_data].values)
print( datos[find_data][numero])