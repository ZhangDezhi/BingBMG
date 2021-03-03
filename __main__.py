#!/usr/bin/env python
# -!- coding: utf-8 -!-
#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2020-01-09 15:00
# Last Modified  : 2020-01-09 15:06:48
# * FileName       : __main__.py
#**************************************************
import urllib.request
import requests         
import os.path
import ctypes
import platform

def save_img(img_url,dirname):
    #保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        #获得图片文件名，包括后缀
        basename = "bingImage.jpg"
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    print("Save", filepath, "successfully!")

    return filepath

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)       
    img_url = r.url # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url

# 设置图片绝对路径 filepath 所指向的图片为壁纸
def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)

def main():
    system=platform.system()
    plat_version=platform.platform()
    if system == 'Windows':
        dirname = "C:\\Users\hwzhao\Pictures\Bing"       # 图片要被保存在的位置
    elif system == 'Linux':
        dirname = "/home/iscs/Pictures/Bing"       # 图片要被保存在的位置

    
    img_url = get_img_url()
    filepath = save_img(img_url, dirname)   # 图片文件的的路径
    if system == 'Windows':
        set_img_as_wallpaper(filepath)
    elif system == 'Linux':
        bashCommand = r"gsettings set org.gnome.desktop.background picture-uri 'file://"+filepath +"'"
        os.system(bashCommand)

main()
