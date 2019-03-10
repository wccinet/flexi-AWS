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
        html = html + '<dl><strong><a>'+crow['Title']+'</a></strong><a> </a><span>|</span><a href="https://d1ytx3lv2b2m7c.cloudfront.net/m/'+crow['Const']+'.html" target="_blank"><img width="16" height="16" style="vertical-align:bottom" src="https://raw.githubusercontent.com/Ede123/userscripts/master/icons/Rotten_Tomatoes.png"></a></dl>'
        f = open('flexi.html','w')
f.write(html)
f.close()
