import sys
import os
import PIL.Image
import PIL.ImageFilter

im = PIL.Image.open("image.png")
# 创建新图像
res = PIL.Image.new (im.mode, (2*im.width, 2*im.height))
# 原先图像放置左上角
res.paste(im, (0,0,im.width,im.height))

contour = im.filter(PIL.ImageFilter.CONTOUR)
res.paste(contour,(im.width,0,2*im.width,im.height))

emboss = im.filter(PIL.ImageFilter.EMBOSS)
res.paste(emboss,(0,im.height,im.width,2*im.height))

edges = im.filter(PIL.ImageFilter.FIND_EDGES)
res.paste(edges,(im.width,im.height,2*im.width,2*im.height))

res.show()