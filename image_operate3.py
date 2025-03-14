import sys
import os
import glob
import PIL.Image

# 指定要处理的图片目录和格式
img_path = sys.argv[1] + "/*." + sys.argv[2]
size = (128, 128)   # 缩略图大小

# 遍历文件并处理
for infile in glob.glob(img_path):
    f, e = os.path.splitext(infile)  # 分割文件名和扩展名
    outfile = f + "_s." + sys.argv[2]           # 生成缩略图文件名
    img = PIL.Image.open(infile)
    img.thumbnail(size, PIL.Image.LANCZOS)
    img.save(outfile)
