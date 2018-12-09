from PIL import Image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)
n = 16
name = "d4"
path = "./pic/"+str(n)+".png"
print("path: "+ path)
oriImg = Image.open(path)
print(oriImg.size)
markImg = Image.new('RGBA',(30,30),'white')
oriImg.paste(markImg,(0,0))
draw = ImageDraw.Draw(oriImg)
draw.text((0, 0), name, (0,0,0), font=font)    #设置文字位置/内容/颜色/字体
draw = ImageDraw.Draw(oriImg)
oriImg.save("save"+ path)
#oriImg.show()

