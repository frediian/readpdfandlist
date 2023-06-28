from pypdf import PdfReader
import pandas as pd
import sys, re

archive= "./pdfs/"+sys.argv[1]+".pdf"

reader = PdfReader(archive)

dicTextos = {}
count=0

# extrayendo datos del pdf

print("Inicia Lectura de archivo PFD's")
for page in reader.pages:
    count +=1
    dicTextos[count]=page.extract_text()[0:500]
    
print("finaliza lectura de ",count," paginas del archivo: ", archive)
print (dicTextos[1])
cedulas_personas = []    
accion_personas = []
numero_personas = []

for acciones in dicTextos:
    ced=re.search("[0-9]{10}", dicTextos[acciones])
    accion = re.search("[0-9]{7}-", dicTextos[acciones])
    cedulas_personas.append(ced[0])
    accion_personas.append(accion[0][0:7])
    numero_personas.append(acciones)

print("Creando archivo de excel")

df = pd.DataFrame({"Nro.":numero_personas,"Cedula": cedulas_personas, "Accion Nro.":accion_personas},index=None)  
nameExcel = "./excel/"+sys.argv[1]+".xlsx"

with pd.ExcelWriter(
    nameExcel,
        engine="xlsxwriter",
 ) as writer:
     df.to_excel(writer, sheet_name="Sheet1", index=False)  

print("Se ha creado Archivo de nombre: ", nameExcel)