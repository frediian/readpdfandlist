import pandas as pd
import sys


archiveExcel= "./excel/"+str(sys.argv[1])+".xls"

datos = pd.read_excel(archiveExcel)

print(len(datos.columns))
print((datos.columns[0]))

find_data = "NÚMERO IDENTIFICACIÓN"
