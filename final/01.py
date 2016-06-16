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
size = width,height=1280,720 #視窗大小
screen = pygame.display.set_mode(size) #視窗初始化
background = pygame.Surface(screen.get_size()) #背景設定-背景大小
background = background.convert() #背景設定
background.fill((250, 250, 250)) #顏色
screen.blit(background, (0, 0)) #畫上去
if img.size[1]<height:
	if img.size[0]>width:
		ratio = float(width)/img.size[0] #照片vs視窗比例
		h = int(img.size[1]*ratio)
		n = img.resize((width, h), Image.BILINEAR)
	else:
		n = img
else:
	if img.size[1]>height:
		ratio = float(height)/img.size[1] #照片vs視窗比例
		w = int(img.size[0]*ratio)
		n = img.resize((w, height), Image.BILINEAR)
	else:
		n = img
mode = n.mode
size = n.size
data = n.tostring()
pic = pygame.image.fromstring(data, size, mode) #用PIL做出來的圖 畫在PYGAME上
picrect = pic.get_rect()
src = ""
dst = ""
ison = 0 #滑鼠有沒有按
usage()
while 1:
    for event in pygame.event.get():
		if event.type == pygame.QUIT: #退出
			sys.exit()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.type == pygame.K_ESCAPE:
				sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			src = pygame.mouse.get_pos()
			ison = 1
			print '%s, %s' % src
		elif event.type == pygame.MOUSEBUTTONUP:
			ison = 0
			dst = pygame.mouse.get_pos()
			if (dst[0]-src[0]!=0 and dst[1]-src[1]!=0):
				n = img.resize((dst[0],dst[1]), Image.BILINEAR)
				mode = n.mode
				size = n.size
				data = n.tostring()
				pic = pygame.image.fromstring(data, size, mode) #用PIL做出來的圖 畫在PYGAME上
				picrect = pic.get_rect()
		if ison == 1:
			si = pygame.mouse.get_pos()
			if (si[0]-src[0]!=0 and si[1]-src[1]!=0):
				x = si[0]
				y = si[1]
				n = img.resize((x,y), Image.BILINEAR)
				mode = n.mode
				size = n.size
				data = n.tostring()
				pic = pygame.image.fromstring(data, size, mode)
				picrect = pic.get_rect()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			n.save('opt.jpg')
			print u"Image has been saved. opt.jpg"
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_u:
			os.system("make_code.py")
    screen.blit(pic,picrect)
    pygame.display.flip()
    screen.blit(background, (0, 0))
	