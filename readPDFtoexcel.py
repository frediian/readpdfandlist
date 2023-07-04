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
    dicTextos[count]=page.extract_text()[0:800]
    
print("finaliza lectura de ",count," paginas del archivo: ", archive)

person_id, person_doc, person_count, brute  = [],[],[],[]

for acciones in dicTextos:
    p_id=re.search("[0-9]{10}\s", dicTextos[acciones][300:800])
    p_doc = re.search("[0-9]{7}-", dicTextos[acciones][0:150])
# registrar solo datos existentes
    if p_id != None and p_doc != None :
        person_id.append(str(p_id[0]))
        person_doc.append(p_doc[0][0:7])
    else:
        person_id.append("")
        person_doc.append("")

    person_count.append(acciones)
    brute.append(dicTextos[acciones])

print("Creando archivo de excel")
df = pd.DataFrame({"Nro.":person_count,"Identification": person_id, "Doc Nro.":person_doc, "data":brute},index=None)  
nameExcel = "./excel/"+sys.argv[1]+".xlsx"

with pd.ExcelWriter( nameExcel, engine="xlsxwriter", ) as writer:
     df.to_excel(writer, sheet_name="Sheet1", index=False)  

print("Se ha creado Archivo de nombre: ", nameExcel)