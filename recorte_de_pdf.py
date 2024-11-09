from PyPDF2 import PdfReader, PdfWriter

# Carrega o PDF
input_pdf = PdfReader("arquitetura-e-organizacao-computadores-8a.pdf")
output_pdf = PdfWriter()

# Define as páginas que deseja extrair
for i in range(264, 300 + 1):
    output_pdf.add_page(input_pdf.pages[i])

# Salva as páginas selecionadas em um novo arquivo PDF
with open("capitulo_extraido.pdf", "wb") as output_file:
    output_pdf.write(output_file)
