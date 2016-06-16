#!usr/bin/env python
# -*- coding: utf-8 -*-
import random
pick = input("要抽多少人?")
f = open("class_list.txt", "r")
dic = {}
choice ={}
while 1:
	line = f.readline()
	if not line:
		break
	str1 = line.replace("\n","")
	str2 = str1.split("\t")
	dic[str2[0]] = str2[1] + str2[2]
M = len(dic)
x = 0
for i in 
# while x < pick:
# 	n = random.randint(1,M)
# 	if choice.has_key(n-1):
# 		continue
# 	else :
# 		choice[n-1] = dic[n-1]
# 		x += 1
# for i in choice.keys():
# 	print i+"-->"+choice[i]
