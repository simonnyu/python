#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import sys,pygame,Image,ImageDraw,tkFileDialog,os
def usage():
	print u"Press the 's' key to save image"
	print u"Press the 'u' key to upload image to imgur"
	print u"Press the 'q' key to exit"

options = {}
options['filetypes'] = [("jpg","*.jpg")]
options['initialdir'] = "c:\\"
options['multiple'] = False
options['title'] = u"開啟檔案"
loc=tkFileDialog.askopenfilename(**options)
if loc:
	imgsrc = "%s" %loc
	imgsrc = imgsrc.replace("/","\\")
else:
	imgsrc = "pic2.jpg"
pygame.init()
img = Image.open(imgsrc) #開圖片
size = width,height=img.size[0],img.size[1] #視窗大小
screen = pygame.display.set_mode(size) #視窗初始化
background = pygame.Surface(screen.get_size()) #背景設定-背景大小
background = background.convert() #背景設定
background.fill((250, 250, 250)) #顏色
screen.blit(background, (0, 0)) #畫上去
n = img.convert("RGBA")
data = n.getdata()
newdata = []
for item in data:
	newdata.append((item[0],item[1],item[2],110))
n.putdata(newdata)
mode = n.mode
size = n.size
data = n.tostring()
pic = pygame.image.fromstring(data, size, mode) #用PIL做出來的圖 畫在PYGAME上
picrect = pic.get_rect()
src = ""
dst = ""
area = ""
ison = 0 #滑鼠有沒有按
tp = 0
usage()
while 1:
    for event in pygame.event.get():
		if event.type == pygame.QUIT: #退出
			sys.exit()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			area = ""
			src = pygame.mouse.get_pos()
			print src
			ison = 1
		elif event.type == pygame.MOUSEBUTTONUP:
			ison = 0
			dst = pygame.mouse.get_pos()
			if (dst[0]-src[0]!=0 and dst[1]-src[1]!=0):
				print dst
				if(dst[0]>src[0] and dst[1]>src[1]):
					tp = 1
					n = img.crop((src[0],src[1],dst[0],dst[1]))
				elif(dst[0]<src[0] and dst[1]<src[1]):
					tp = 2
					n = img.crop((dst[0],dst[1],src[0],src[1]))
				elif(dst[0]<src[0] and dst[1]>src[1]):
					tp =3
					n = img.crop((dst[0],src[1],src[0],dst[1]))
				elif(dst[0]-src[0]>0 or dst[1]-src[1]<0):
					tp =4
					n = img.crop((src[0],dst[1],dst[0],src[1]))
				mode = n.mode
				size = n.size
				data = n.tostring()
				area = pygame.image.fromstring(data, size, mode)
				if(tp==1):
					screen.blit(area,(src[0],src[1])) #用PIL做出來的圖 畫在PYGAME上
				elif(tp==2):
					screen.blit(area,(dst[0],dst[1]))
				elif(tp==3):
					screen.blit(area,(dst[0],src[1]))
				elif(tp==4):
					screen.blit(area,(src[0],dst[1]))
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			n.save('opt.jpg')
			print u"Image has been saved. opt.jpg"
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_u:
			os.system("make_code.py")
    screen.blit(pic,(0,0))
    if(area != "" and tp==1):
    	screen.blit(area,(src[0],src[1]))
    elif(area != "" and tp==2):
    	screen.blit(area,(dst[0],dst[1]))
    elif(area != "" and tp==3):
    	screen.blit(area,(dst[0],src[1]))
    elif(area != "" and tp==4):
    	screen.blit(area,(src[0],dst[1]))
    pygame.display.flip()
    screen.blit(background, (0, 0))
	