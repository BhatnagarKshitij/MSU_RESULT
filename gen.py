from PIL import Image, ImageDraw, ImageFont
import os,glob
import numpy as np
import random

parentPath=r"CaptchaDataset\\"


charactersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
fontTypes=[]

for font in glob.glob("fonts\\*"):
    fontTypes.append(os.path.abspath(font))
    
for index,character in enumerate(charactersList):
    
    path=os.path.join(parentPath,character+"_"+str(index))
    os.mkdir(path)
    
    
    for imageCounter in range(len(fontTypes)):
        for repeats in range(3):
            img = Image.new('1', (28, 28), color = 'black')
            fnt = ImageFont.truetype(fontTypes[imageCounter], random.randint(30,50))
            w,h=fnt.getsize(character)
            d = ImageDraw.Draw(img)
            d.text((0,0), character, font=fnt, fill=(255),align="center")
            img=np.pad(img,pad_width=10, mode='constant', constant_values=0)
            img=Image.fromarray(img)
            img=img.rotate(random.randint(0,30))
            img.save(path+"\\"+str(imageCounter)+"_"+str(repeats)+".jpg")

