from libretranslatepy import LibreTranslateAPI
import PyPDF2
from fpdf import FPDF
translator = LibreTranslateAPI()

pdfFileObj = open('sample.pdf','rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))
page1 = pdfReader.pages[0]
ext_text = page1.extract_text()
translated_text = translator.translate(ext_text, "en", "de")

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
line_height = 5
pdf.multi_cell(0, line_height, translated_text )
    
pdf.output('output.pdf')