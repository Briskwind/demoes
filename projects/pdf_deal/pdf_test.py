import os
from conf import BASE_DIR
from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = os.path.join(BASE_DIR, 'projects', 'pdf_deal', 'Python_Cookbook.pdf')

# 创建 pdf 用，要加密只能重新创建
pdf_output = PdfFileWriter()
pdf_input = PdfFileReader(open(file_path, 'rb'))
page_count = pdf_input.getNumPages()

for i in range(page_count):
    # 将 read 对象中的内容增加入 write 对象中
    pdf_output.addPage(pdf_input.getPage(i))

# 进行加密比较费时 5秒左右，有没有办法优化
pdf_output.encrypt('123456', use_128bit=False)
outfn = 'Python_Cookbook_encrypted.pdf'

pdf_output.write(open(outfn, 'wb'))
