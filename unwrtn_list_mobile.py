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
        html = html + '<dl><a href="https://d1ytx3lv2b2m7c.cloudfront.net/title/'+crow['Const']+'.html" alt="flexi TV-R">'+crow['Title']+'</a></dl>'
        f = open('flexi.html','w')
f.write(html)
f.close()
