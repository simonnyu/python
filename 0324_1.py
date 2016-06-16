#!usr/bin/env python
# -*- coding: utf-8 -*-
f = open("record.txt", "r")
x = {}
while 1:
	line = f.readline();
	if not line:
		break
	str1 = line.replace("\n","")
	str2 = str1.split(",")
	if x.has_key(str2[0]):
		x[str2[0]] = int(x[str2[0]])+int(str2[1])
	else :
		x[str2[0]] = int(str2[1])
for i in x.keys():
	print i+"-->"+str(x[i])