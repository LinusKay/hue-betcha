# Adapted from code by Mark Ransom: https://stackoverflow.com/a/24875271
# input_image takes an image file
# input_num takes the number of images to output
# program will increment hue shift value between 0 - 360 with each output

import colorsys
from wsgiref.util import shift_path_info
from PIL import Image

input_image = input('image: ')
input_num = int(input('number of outputs: '))
shift_size = 360/input_num

for i in range(input_num):
    im = Image.open(input_image)
    ld = im.load()
    width, height = im.size
    for y in range(height):
        for x in range(width):
            r,g,b,a = ld[x,y]
            h,s,v = colorsys.rgb_to_hsv(r/255., g/255., b/255.)
            h = (h + -(shift_size * i)/360.0) % 1.0
            s = s**0.65
            r,g,b = colorsys.hsv_to_rgb(h, s, v)
            ld[x,y] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999), a)
    im.save(str(i) + '.png')