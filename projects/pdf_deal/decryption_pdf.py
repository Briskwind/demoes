import os
from conf import BASE_DIR

file_path = os.path.join(BASE_DIR, 'projects', 'pdf_deal', 'encrypted.pdf')


file_path_2 = os.path.join(BASE_DIR, 'projects', 'pdf_deal', 'Python_Cookbook.pdf')

pdfFile = open(file_path_2, 'rb')
content = pdfFile.read()
print('content', content)
