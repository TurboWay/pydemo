#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/25 14:14
# @Author : way
# @Site : 
# @Describe: docx , pdf 文件解析

import base64
import docx
from io import BytesIO

filename = r"C:\Users\Administrator\Desktop\1.docx"
# with open(filename, 'rb') as f:
#     file = BytesIO(f.read())
# with open(filename, 'rb') as f:
#     st = base64.b64encode(f.read())
#     file = BytesIO(base64.b64decode(st))
doc = docx.Document(filename)
paras = [para.text for para in doc.paragraphs if para.text]
content = ';'.join(paras)
print(content)


import pdfplumber

filename = r"C:\Users\Administrator\Desktop\8E06BBABF68CA632DC0820E4DC110E4E.pdf"
# with open(filename, 'rb') as f:
#     file = BytesIO(f.read())
# with open(filename, 'rb') as f:
#     st = base64.b64encode(f.read()).decode()
#     file = BytesIO(base64.b64decode(st))
pdf = pdfplumber.open(filename)
paras = [page.extract_text() for page in pdf.pages if page.extract_text()]
content = ';'.join(paras)
print(content)

# doc 解析, win 可以使用 win32com 先把 doc 转 docx ; centos 可以使用 antiword