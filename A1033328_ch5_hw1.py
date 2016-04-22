#!usr/bin/env python
# -*- coding: utf-8 -*-
import re
i = raw_input("請輸入會員卡號，1個大寫英文字-6碼數字: ")
while re.findall(r"[A-Z]{1}-\d{6}",i)==[]:
        i = raw_input("請輸入會員卡號，1個大寫英文字-6碼數字: ")
a = "E-056790"
if(i==a):
        print "恭喜您中了10萬元"
elif(re.findall(r"E-[0-9]56790",i)):
        print "恭喜您中了2萬元"
elif(re.findall(r"[A-z]{1}-\d{3}790",i)):
        print "恭喜您中了100元購物禮券"
else:
        print "銘謝惠顧"
