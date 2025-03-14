import PIL; from PIL import Image
import PIL.Image

# 打开并显示图像
im = PIL.Image.open("image.png")
im.show()
# 显示图像格式信息
print(im.format, im.size, im.mode)

