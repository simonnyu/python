#!usr/bin/env python
# -*- coding: utf-8 -*-
f = open("input.txt","r")
blank = 0
e = 0
total = 0
while 1:
	line = f.readline()
	if not line:
		break
	blank += line.count(" ")
	e += line.count("e")
	total += len(line)
print "Total blank %d"%blank
print "Total e %d"%e
e_percentage = (float(e)/total)
b_percentage = (float(blank)/total)
print "e/total: %f"%e_percentage
print "blank/total %f"%b_percentage