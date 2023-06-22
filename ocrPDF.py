from PIL import Image
from pypdf import PdfReader, PdfWriter

import pytesseract


reader = PdfReader("./pdfs/1.PDF")

page = reader.pages[1]
pdf = pytesseract.image_to_pdf_or_hocr(page.__hash__, extension='pdf')
with open('1TEST.pdf', 'w+b') as f:
    f.write(pdf)