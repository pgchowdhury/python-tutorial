"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 21-Nov-2024
    Project: Merge PDFs
    Library: pypdf -- pip install pypdf
"""
from pypdf import PdfWriter

def pdf_merger(location, lst_pdf, lst_pdf_page):
    merger = PdfWriter()
    for pdf, pdf_page in zip(lst_pdf, lst_pdf_page):
        merger.append(f'{location}/{pdf}', pages= pdf_page)
    merger.write(f'{location}/merged.pdf')
    print("PDFs merged successfully !")

if __name__ == '__main__':
    location = 'automation/pdfmerger'
    lst_pdf = ['python.pdf', 'java.pdf', 'go.pdf']
    lst_pdf_page = [(0, 2), (0, 1), [1]]
    pdf_merger(location, lst_pdf, lst_pdf_page)
