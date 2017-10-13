from PIL import Image

# 打开一张当路径下的图片
im = Image.open('a.jpg')
# 获取此图片的信息
print(im.format, im.size, im.mode)

# 生成缩略图
im.thumbnail((200, 130))
im.save('a1.jpg', 'JPEG')
