# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 08:55:14 2020

@author: 15025

Text nesting of holiday wishes , two-level nesting.
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class newYear:
    def __init__(self):
        self.word_size = 25
        self.word1 = "新"
        self.word2 = "年"
        self.word3 = "快"
        self.word4 = "乐"
        self.image1 = None
        self.image2 = None
        self.image3 = None
        self.image4 = None
        self.component1 = None
        self.component2 = None
    
    
    def imageDraw(self, word):
        image1 = Image.new("RGB", (self.word_size, self.word_size), "white").convert("L")

        work_bench = ImageDraw.Draw(im=image1)

        work_bench.text(xy=(0, 0), text=u'{}'.format(word), fill="#000000", font=ImageFont.truetype('C:/Windows/Fonts/simsun.ttc', self.word_size))

        return image1                         
    
    
    def createComponent(self, image1, image2):
        bench_size = (pow(self.word_size, 2), pow(self.word_size, 2))
        new_bench = Image.new('L', bench_size, "white")
        for w in range(image1.width):
            for h in range(image1.height):
                if image1.getpixel((w, h)) < 127:
                    new_bench.paste(image2, (w * image2.width, h * image2.height))
        
        return new_bench
        
        
    def mergeComponent(self):
        bench_size = (1300, 800)

        new_bench = Image.new('L', bench_size, "white")
        
        new_bench.paste(self.component1, (0, 0))
        new_bench.paste(self.component2, (700, 0))
        
        new_bench.save("C:/Users/15025/Desktop/blessing.jpg")
        
    def createBlessing(self):
        self.image1 = self.imageDraw(self.word1)
        self.image2 = self.imageDraw(self.word2)
        self.image3 = self.imageDraw(self.word3)
        self.image4 = self.imageDraw(self.word4)
        
        self.component1 = self.createComponent(self.image1, self.image3)
        self.component2 = self.createComponent(self.image2, self.image4)
        
        self.mergeComponent()
        

class wordBlessing:
    unit_dict = {
        "newyear": newYear
    }

    @classmethod
    def create_unit(cls, unit_type):
        return cls.unit_dict.get(unit_type)()


class App:
    blessing = wordBlessing

    def blessingMake(self, blessing_type):
        unit = self.blessing.create_unit(blessing_type)
        unit.createBlessing()


if __name__ == "__main__":
    app = App()
    app.blessingMake("newyear")
