#!usr/bin/env python
# -*- coding: utf-8 -*-
def isPrime(N):
	global n
	n = 0
	if N==2:
		n = 1
	else:
		for x in range(2,N):
			if (N%x==0):
				n = 0
				break
			else:
				n = 1
	return n
sum_n = 0
count = 0
for x in range(2,1001):
	if isPrime(x):
		sum_n += x
		count += 1
print "sum of prime in 2~1000 ----> %d"%sum_n