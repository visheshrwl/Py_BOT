import numpy as np
import cv2 

width, height = 800, 800

# Create a Blank Image
img = np.zeros((height, width))

location = 0
shade = 0
n_shades = 255

for i in range(n_shades):
    img[0:height, location:location+width//n_shades] = shade
    location += width//n_shades
    shade += 255//n_shades

#
cv2.imwrite("my_img.png", img)