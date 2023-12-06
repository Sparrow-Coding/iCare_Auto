
# import fitz  # PyMuPDF
import pandas as pd

# pdf_path = 'Desktop/iCare.pdf'
# csv_path = 'Desktop/iCare.csv'

# text = ""

pdf_document = fitz.open(pdf_path)

for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    text += page.get_text()

pdf_document.close()

with open(csv_path, "w", encoding="utf-8") as csv_file:
    csv_file.write(text)

df3 = pd.read_csv('Desktop/iCare.csv')
print(df3.head())