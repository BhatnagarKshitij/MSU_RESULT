from PIL import Image, ImageDraw, ImageFont
import os,glob

parentPath=r"CaptchaDataset\\"


charactersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
fontTypes=[]

for font in glob.glob("fonts\\*"):
    fontTypes.append(os.path.abspath(font))
    
for index,character in enumerate(charactersList):
    
    path=os.path.join(parentPath,character+"_"+str(index))
    os.mkdir(path)
    
    
    for imageCounter in range(len(fontTypes)):
        img = Image.new('1', (80, 80), color = 'black')
        fnt = ImageFont.truetype(fontTypes[imageCounter], 115)
        w,h=fnt.getsize(character)
        d = ImageDraw.Draw(img)
        d.text(((80-w)/2,((80-h)/2)-5), character, font=fnt, fill=(255),align="center")
        img.save(path+"\\"+str(imageCounter)+".jpg")

