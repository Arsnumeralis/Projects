import PyPDF2

file = PyPDF2.PdfFileReader(open('Projects\pdf_watermarker\lorem_ipsum.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('Projects\pdf_watermarker\wtr.pdf', 'rb'))
result = PyPDF2.PdfFileWriter()

for i in range(file.getNumPages()):
    page = file.getPage(i)
    page.mergePage(watermark.getPage(0))
    result.addPage(page)

    with open('watermarked.pdf', 'wb') as all_gud:
        result.write(all_gud)
# pdfs = [file, watermark]

# def watermarker(file1, file2):
#     output = PyPDF2.PdfFileMerger()
#     output.merge(0, file1, file2)
#     print(output)

# watermarker(file, watermark)