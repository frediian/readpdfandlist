import os
import readPDFtoexcel as rx
docs = os.listdir('./pdfs')

for n in docs:
    print(n)
    rx()
