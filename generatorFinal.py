from PIL import Image, ImageDraw, ImageFont
import os,glob
import numpy as np
import random

parentPath=r"CaptchaDataset\\"


charactersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
fontTypes=[]

for font in glob.glob("fonts\\***\*.ttf"): # Create Image for every font
    fontTypes.append(os.path.abspath(font))
    
print(len(fontTypes))
    
for index,character in enumerate(charactersList):
    
    
    path=os.path.join(parentPath,character+"_"+str(index))
    os.mkdir(path)
    
    
    for imageCounter in range(len(fontTypes)):
        fontSize=70
        print("Creating Dataset for : "+character+" Image Counter = "+str(imageCounter))
        
        fnt = ImageFont.truetype(fontTypes[imageCounter],fontSize)
        w,h=fnt.getsize(character)
        
        while not (h>=80 and h<=95):
            fontSize+=1
            fnt = ImageFont.truetype(fontTypes[imageCounter],fontSize)
            w,h=fnt.getsize(character)
        print(fontSize)
        img = Image.new(mode="1",size=(80, h), color = 'black')
        d = ImageDraw.Draw(img)
        w,h=fnt.getsize(character)
        d.text(((80-w)/2,0), character, font=fnt, fill=(255),align="center") #TO ALIGN CHARACTER IN CENTER
        img.save(path+"\\"+str(character)+"_"+str(imageCounter)+".jpg")


