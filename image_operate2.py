import sys
import os
import glob
import PIL.Image

img_path = sys.argv[1] + "/*." + sys.argv[2]
for infile in glob.glob(img_path):
  f,e = os.path.splitext(infile)
  outfile = f + "." + sys.argv[3]
  PIL.Image.open(infile).save(outfile)