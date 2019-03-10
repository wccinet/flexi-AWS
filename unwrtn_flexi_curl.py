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
        html = html + 'curl "https://api.scraperapi.com?key=xxxxxxxxxxxxxxx&url=https://www.imdb.com/title/'+crow['Const']+'&keep_headers=true" > '+crow['Const']+'.html\n'
        f = open('flexi.sh','w')
f.write(html)
f.close()
