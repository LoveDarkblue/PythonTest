import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter


def getChar():
    return chr(random.randint(65, 90))


def getColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def getColor1():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60
imgbg = Image.new('RGB', (width, height), (255, 255, 255))
# 字体和大小
fonttype = ImageFont.truetype('comic.ttf', 30)
# 创建画笔工具
draw = ImageDraw.Draw(imgbg)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=getColor())
for t in range(4):
    draw.text((60 * t + 10, 10), getChar(), font=fonttype, fill=getColor1())
# 加点效果增加识别难度
imgbg = imgbg.filter(ImageFilter.EMBOSS)
imgbg.save('co.jpg', 'jpeg')
