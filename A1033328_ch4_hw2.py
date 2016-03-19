#!usr/bin/env python
# -*- coding: utf-8 -*-
import random
secert = random.randint(1,99)
print "終極密碼~~"
count = 0
m = 1
M = 99
while 1:
	ans = input("請輸入你要猜的數字")
	if secert > ans:
		m = ans
		print "現在的範圍是%d~%d"%(m,M)
		count += 1
	elif secert < ans:
		M = ans
		print "現在的範圍是%d~%d"%(m,M)
		count += 1
	elif secert == ans:
		print "哇!你猜到了!! 終極密碼是%d,你花了%d次猜中。"%(secert,count)
		break