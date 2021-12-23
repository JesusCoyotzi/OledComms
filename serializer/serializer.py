#Serializer for 128*32 screen SD1306
from PIL import Image
import numpy as np
from scipy import signal

import argparse
import os
import sys

import matplotlib.pyplot as plt

def strided_convolution(image, weight, stride):
    im_h, im_w = image.shape
    f_h, f_w = weight.shape
    stride_h, stride_w = stride
    out_shape = (1 + (im_h - f_h) // stride_h, 1 + (im_w - f_w) // stride_w, f_h, f_w)
    out_strides = (image.strides[0] * stride_h, image.strides[1] * stride_w, image.strides[0], image.strides[1])
    windows = np.lib.stride_tricks.as_strided(image, shape=out_shape, strides=out_strides)

    return np.tensordot(windows, weight, axes=((2, 3), (0, 1)))

if __name__=="__main__":
  parser = argparse.ArgumentParser(description="Image serializer")
  parser.add_argument('image',type=str,help='Input image')
  parser.add_argument('--output',type=str,help='Output txt file',default='')
  parser.add_argument('--height',type=int, help='Height of screen',default=32)
  parser.add_argument('--width',type=int, help='Width of screen',default=128)
  parser.add_argument('--viz',action='store_true')
  args = parser.parse_args()
  with Image.open(args.image) as im:
    print("Image statistics:")
    print(im.size,im.format)
    if im.size[0] > args.width or im.size[1] > args.height:
      print("ERROR, image wont fit in screen, modify values or resize")
      sys.exit(1)
 
    np_image = np.array(im,dtype=int)
    if im.mode == '1':
      np_image=np_image*255
    

  print(np_image)
  #Inversion and normalizing:
  np_image = np_image/255
  np_image = 1 - np_image
  #Padding, only height padding is needed. ?
  pad_y = args.height - np_image.shape[0]
  pad_x = args.width - np_image.shape[1]
  #Default is zero
  np_image = np.pad(np_image,[(0,pad_y),(0,pad_x)],mode='constant',constant_values=0) 
  
  if args.viz:
    plt.imshow(np_image)
    plt.show() 
#    with np.printoptions(linewidth=2000,edgeitems=30):
#      print(np_image)

  pixel_per_byte=8
  
  char_filter = 2**np.arange(pixel_per_byte)
  char_filter =  char_filter.reshape(8,1)
  
  np_chars =  strided_convolution(np_image,char_filter,(8,1))
 
  if args.viz: 
    with np.printoptions(linewidth=2000,edgeitems=30):
      print(np_chars)
      #print(np_chars.view('c'))

  print("Serialized image for ({},{})".format(args.height,args.width))
  print("Array: {} @ {} bits per row".format(np_chars.shape,pixel_per_byte))
  if args.output:
    print('hola')
    np.savetxt(args.output,np_chars,fmt='%3d',delimiter=',')
  else:
    basename = os.path.splitext(args.image)[0]  
    np.savetxt(basename+".oled",np_chars,fmt='%3d',delimiter=',')
  
  
