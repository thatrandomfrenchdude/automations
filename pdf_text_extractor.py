# https://python.plainenglish.io/10-python-automation-scripts-for-daily-problems-68991d28f490

# PDF Text Extractor
# pip install PyMuPDF
import fitz as pdfExtract
def Text_Extractor(pdfFile):
    # Open the PDF file
    pdf_doc = pdfExtract.open(pdfFile)
    # Get the total number of pages in the PDF
    pages = pdf_doc.page_count
    # Extract text from each page
    for page_no in range(pages):
        page = pdf_doc.load_page(page_no)
        text = page.get_text()
        print(f"Page {page_no + 1}:\n{text}\n")
Text_Extractor("sample.pdf")