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
        html = html + 'folder.createFile(\''+crow['Const']+'\',\'<!DOCTYPE html><head> flexi TV-R [sign-in] '+crow['Const']+'</head><meta http-equiv="refresh" content="0;URL=https://www.google.com/accounts/AccountChooser?Email='+crow['URL']+'&continue=https://docs.google.com/a/unwr.tn/document/d/e/2PACX-1vTCahFYjxwjW1PKQdC7W41ia6Zz7H8jEOqFB8SYYSGz0PM8gnwu0npjbm6AdWn1cqy4G9wmApUa0qde/pub"><img src="data:image/jpeg;base64,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" alt="base64 cable">'+'\')\n'
        f = open('flexi.html','w')
f.write(html)
f.close()
