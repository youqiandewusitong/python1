import fitz

pdf="C:\\Users\\吴思彤\\Desktop\\PDF 宁晓坤 - 副本.pdf"
doc=fitz.open(pdf)
for page in doc:
    pix=page.get_pixmap()
    pix.save('zhaopian -%i.png'%page.number)
doc.close()