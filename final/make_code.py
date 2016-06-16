#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyimgur,pyqrcode

CLIENT_ID = "ef229a6b416a5b6"
client_secret = "fda1fbbfeca02638b5c684eaee499cec90954756"
PATH = "opt.jpg"
im = pyimgur.Imgur(CLIENT_ID,client_secret)
uploaded_image = im.upload_image(PATH,title="Uploaded with PyImgur")
print(uploaded_image.link)

a=pyqrcode.create(uploaded_image.link) #產生一個QRcode
#a.svg('nukim.svg', scale=10)#將QRcode變成svg。scale越大，QRcode越大
a.svg('zzz.svg', scale=10,module_color="#FFFFFF", background=(0xff, 0xff, 0xcc),title="1234567890")
a.png('res.png', scale=6, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xcc])
