from libretranslatepy import LibreTranslateAPI
import PyPDF2
from fpdf import FPDF
translator = LibreTranslateAPI()
pdf = FPDF()
pdfFileObj = open('sample.pdf','rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
page_num = len(pdfReader.pages)
for page_number in range(page_num):   
    page = pdfReader.pages[page_number]
    page_content = page.extract_text()
    paragraphs = page_content.split('\n')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    for p in paragraphs:
        translated_text = translator.translate(p, "en", "de")
        pdf.multi_cell(0, 5, translated_text )
    pdf.ln()
pdf.output('output.pdf')