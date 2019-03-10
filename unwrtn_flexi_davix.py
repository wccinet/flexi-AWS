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
        html = html + 'davix-put --s3accesskey xxxxxxx --s3secretkey yyyyyyyyy --s3alternate '+crow['Const']+'.html s3://s3-ap-southeast-2.amazonaws.com/newsact-repositories/title/'+crow['Const']+'.html\n'
        f = open('flexi.sh','w')
f.write(html)
f.close()
