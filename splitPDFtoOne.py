import pandas as pd
import sys

archive= "./excel/"+str(sys.argv[1])+".xlsx"

datos = pd.read_excel(archive)
print (datos.shape[0])

print (datos[datos.columns[2]][0])