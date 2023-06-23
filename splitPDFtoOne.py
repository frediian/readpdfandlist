from pypdf import PdfReader, PdfWriter
import pandas as pd
import sys

archiveExcel= "./excel/"+str(sys.argv[1])+".xlsx"
archivePDF= "./pdfs/"+str(sys.argv[1])+".pdf"

inputFile = PdfReader(archivePDF)

datos = pd.read_excel(archiveExcel)
nro_personas = datos.shape[0]

for persona in range (nro_personas):
    namepdf = "docs/ap_-_"+str(datos[datos.columns[2]][persona])+".pdf"
    outputFile = PdfWriter()
    outputFile.add_page(inputFile.pages[persona])
    outputFile.write(namepdf)
    outputFile.close()

#print (datos[datos.columns[2]][0])