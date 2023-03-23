import numpy as np
from PIL import Image

width, height = 600, 800

# Create a Blank Image
img = np.zeros((height, width, 3), dtype=np.uint8)

img[:] = (35, 29, 43)
img[int(height*0.85):height, 0:width] = (35,55,43)
# drawing the building
img[int(height*0.1):int(height*0.9), int(width*0.2):int(width*0.8)] = (94,101,107)

#draw windows
for row in range(6):
    for column in range(5):
        if np.random.randint(0,8) == 5:
            window_colour = (240,230,140)
        else :
            window_colour = (28,23,35)

        img[int(height*0.1 +100*row + 20 ):int(height*0.1 + 60 + 20 +100*row),
            int(width*0.2 + 75*column + 15):int(width*0.2 + 30 + 15 + 75*column)
            ] = window_colour
        



Image.fromarray(img).save("my_img.png")