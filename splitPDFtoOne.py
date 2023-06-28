from pypdf import PdfReader, PdfWriter
import pandas as pd
import sys, os

archiveExcel= "./excel/"+str(sys.argv[1])+".xlsx"
archivePDF= "./pdfs/"+str(sys.argv[1])+".pdf"

inputFile = PdfReader(archivePDF)

datos = pd.read_excel(archiveExcel, dtype='str')
nro_personas = datos.shape[0]

folder_docs= os.getcwd() + "\\docs\\"

for persona in range (nro_personas):
        namepdf = "ap_-_"+str(datos[datos.columns[2]][persona])+".pdf"
        name_folder = folder_docs + namepdf
        outputFile = PdfWriter()
        outputFile.add_page(inputFile.pages[persona])
        outputFile.write(name_folder)
        outputFile.close()

#print (datos[datos.columns[2]][0])