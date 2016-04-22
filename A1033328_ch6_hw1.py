#!usr/bin/env python
# -*- coding: utf-8 -*-
class Prof:
	def __init__(self,name):
		self.name = name

	said = "我一點都不會介意XD"
	def good(self,g):
		self.g = g
		print self.name+"的專長為"+g

class Stud(Prof):
	def interest(self,i):
		self.i = i
		print self.name+"的興趣為"+i

p1 = Prof("教授")
p1.good("C語言")
p1.good("電腦網路")
s1 = Stud("學生")
s1.good("C語言 電腦網路")
s1.interest("python")
print p1.said
print s1.said