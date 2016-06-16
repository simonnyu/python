#!usr/bin/env python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
f = open("mycourse.html","r")
r = open("result_my.csv","w")
soup = BeautifulSoup(f, 'html.parser')
result = soup.find_all('td', height=re.compile("20"))
cont = ""
x = 0
s = "class\n"
r.write(s)
while x < len(result):
        tmp = str(result[x]).replace('&amp','')
        tmp = tmp.replace('<td align="center" bgcolor="#FFDCD7" height="20" valign="middle">', '')
        tmp = tmp.replace('</td>','')
        tmp = tmp.replace('<td align="center" bgcolor="#FFFFFF" height="20" valign="middle">','')
        r.write(tmp+'\n')
        x += 1
r.close()
f.close()