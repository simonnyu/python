#!usr/bin/env python
# -*- coding: utf-8 -*-
balance = 5000
withdraw = input("請輸入提款金額")
result = balance - withdraw
f = open("ATM.txt", "w")
if (result<0):
        ans = "您的存款不足!!"
elif (result==0) :
        ans = "您的存款無剩餘存款"
elif (result>0) :
        ans = "您的存款還剩%d元"%result
print ans
f.write(ans)
f.close()