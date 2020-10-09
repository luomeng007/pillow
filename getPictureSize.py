# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 07:52:13 2020

@author: 15025
"""

from PIL import Image


class Debug:
    def __init__(self):
        self.path = "C:/Users/15025/Desktop/1.png"
    
    def getPictureSize(self):
        pic = Image.open(self.path)
        print(type(pic))            # <class 'PIL.JpegImagePlugin.JpegImageFile'>
        print(pic.size)             # (960, 960)
        
        
if __name__ == "__main__":
    main = Debug()
    main.getPictureSize()