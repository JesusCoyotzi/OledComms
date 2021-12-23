from PIL import Image 
from PIL import ImageSequence

import argparse
import os

if __name__=="__main__":
  parser = argparse.ArgumentParser(description="Image binarizer")
  parser.add_argument('image',type=str,help='Input image')
  parser.add_argument('threshold',type=int, help='Gray Scale value cut-off')
  parser.add_argument('--height',type=int, help='Height resizing, keeps aspect ratio')
  parser.add_argument('--outfile',type=str,help='Outfile name, with extension')
  
  args = parser.parse_args()
  with Image.open(args.image) as im:
    print("Using image: {}".format(args.image))
    print(im.format, im.size, im.mode)
    threshold = args.threshold
    im_bnw = im.convert('L')
    im_bn = im_bnw.point(lambda p: p > threshold and 255)  
    if args.height:
      h = args.height
      aspect_ratio = float(im_bn.size[0])/im_bn.size[1]    
      im_bn = im_bn.resize((round(h*aspect_ratio),h))
    print("Output:")
    print(im_bn.format, im_bn.size, im_bn.mode)
    if args.outfile:
      im_bn.save(args.outfile)    
    else:
      im_bn.show()
