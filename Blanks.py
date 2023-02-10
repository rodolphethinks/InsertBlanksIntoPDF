from pypdf import PaperSize, PdfReader, PdfWriter

pdf_reader = PdfReader("input.pdf")
pdf_writer = PdfWriter()
pdf_writer.append_pages_from_reader(pdf_reader)

# Loop through all the pages in the input PDF
for i in range (len(pdf_reader.pages)):
    # height then width -> landscape
    pdf_writer.insert_blank_page(PaperSize.A4.height, PaperSize.A4.width, 2*i-1)

with open("output.pdf", "wb") as output_stream:
    pdf_writer.write(output_stream)
