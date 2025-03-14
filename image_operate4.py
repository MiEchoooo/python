# 批量加文字水印 
import sys
import os
import glob
from PIL import Image,ImageDraw,ImageFont

img_path = sys.argv[1] + "/*." + sys.argv[2]
# 保存后缀
img_suffix = sys.argv[2]
# 保存用户输入的水印文字
txt_log = sys.argv[3]
# 遍历所有匹配img_path的图片路径
for infile in glob.glob(img_path):
  f,e = os.path.splitext(infile)
  outfile = f + "_w." + img_suffix
  im = Image.open(infile)
  im_log = Image.new('RGBA',im.size)
  fnt = ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
  d = ImageDraw.ImageDraw(im_log)
  d.text((0,0),txt_log,font=fnt)
  # 将水印图层im_log和原图im合成
  im_out = Image.composite(im_log,im,im_log)
  im_out.save(outfile)
