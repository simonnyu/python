#!usr/bin/env python
# -*- coding: utf-8 -*-
num = input("Plese input an integer:")
for x in range(2,num):
	if (num%x==0):
		n = 0
		break
	else:
		n = 1
if(n==0):
	print "%d isn't a prime"%num
else:
	print "%d is a prime"%num