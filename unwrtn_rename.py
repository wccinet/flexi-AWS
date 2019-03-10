#!/usr/bin/python2.7
from itertools import izip
import csv
import os.path

html = ''
csvfile = open('flexi.csv', 'rb')
reader = csv.reader(csvfile)
headers = None

for row in reader:
    if reader.line_num == 1:
        headers = row
    else:
        crow = dict(zip(headers, row))
        html = html + 'if (file_Id == \''+crow['URL']+'\') { file.setName(\''+crow['Const']+'\');}\n'
        f = open('flexi.html','w')
f.write(html)
f.close()
