# -*- coding:utf-8 -*-

__author__ = 'TianShuo'

import urllib, os
from PIL import Image


def download():
    for i in range(50):
        url = 'http://202.119.248.199/CheckCode.aspx' #验证码的地址
        print "download", i
        file("./pic/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())


def process2value():
    j = 1
    dir = "./pic/"
    path = "./font/"
    for f in os.listdir(dir):
        if f.endswith(".gif"):
            img = Image.open(dir + f) # 读入图片
            img = img.convert("RGBA")
            pixdata = img.load()
            #二值化
            for y in xrange(img.size[1]):
                for x in xrange(img.size[0]):
                    if pixdata[x, y][0] < 90:
                        pixdata[x, y] = (0, 0, 0, 255)
            for y in xrange(img.size[1]):
                for x in xrange(img.size[0]):
                    if pixdata[x, y][1] < 136:
                        pixdata[x, y] = (0, 0, 0, 255)
            for y in xrange(img.size[1]):
                for x in xrange(img.size[0]):
                    if pixdata[x, y][2] > 0:
                        pixdata[x, y] = (255, 255, 255, 255)
            img.save(path + f, "GIF")


def process2():
    j = 1
    dir = "./font/"
    path = "./res/"
    for f in os.listdir(dir):
        if f.endswith(".gif"):
            img = Image.open(dir + f) # 读入图片
            img = img.convert("RGBA")
            pixdata = img.load()
            #二值化
            for y in xrange(img.size[1] - 1):
                for x in xrange(img.size[0] - 1):
                    if x > 0 and y > 0:
                        black = 0
                        if pixdata[x - 1, y] == (255, 255, 255, 255):
                            black = black + 1
                        if pixdata[x, y - 1] == (255, 255, 255, 255):
                            black = black + 1
                        if pixdata[x + 1, y] == (255, 255, 255, 255):
                            black = black + 1
                        if pixdata[x, y + 1] == (255, 255, 255, 255):
                            black = black + 1

                        if pixdata[x, y] == (0, 0, 0, 255) and black > 2:
                            print u'原：x:', x, u'y:', y, pixdata[x, y]
                            pixdata[x, y] = (255, 255, 255, 255)
                            print u'现：x:', x, u'y:', y, pixdata[x, y]

                        if pixdata[x, y] != (0, 0, 0, 255) and pixdata[x, y] != (255, 255, 255, 255):
                            pixdata[x, y] = (255, 255, 255, 255)
                            print u'现：x:', x, u'y:', y, pixdata[x, y],'修正未正确二值化的点'

            img.save(path + f, "GIF")


process2()