#!usr/bin/env python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
f = open("source.html","r")
r = open("result.csv","w")
soup = BeautifulSoup(f, 'html.parser')
result = soup.find_all('a', href=re.compile("tcontent"))
cont = ""
x = 0
s = "OpenYear,Helf,Sclass,Cono,Cname\n"
r.write(s)
while x < len(result):
        tmp = str(result[x]).replace('&amp','')
        tmp = tmp.replace('<a href="tcontent.asp?', '')
        tmp = tmp.replace('" target="_blank">',';Cname=')
        tmp = tmp.replace('</a>','')
        tmp = tmp.replace('OpenYear=','')
        tmp = tmp.replace('Helf=','')
        tmp = tmp.replace('Sclass=','')
        tmp = tmp.replace('Cono=','')
        tmp = tmp.replace('Cname=','')
        tmp = tmp.replace(';',',')
        r.write(tmp+'\n')
        x += 1
r.close()
f.close()