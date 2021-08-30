import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

key_r = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_b = " abcdefghijklmnopqrstuvwxyz"
key_g = " 1234567890!?.,:;'-+"


input_mes = "Yay! You've decoded this message! Of course I knew you can do that ;V. I want to congratulate you! To the best bro I've ever had: Happy Birthday! Tomas! I wish you to acieve your goals! Work it harder, make it better, do it faster makes us stronger, with the power of programming and automatisation ;V Your comrade U+262D"
out_r = []
out_b = []
out_g = []

for letter in input_mes:
    if key_r.find(letter) == -1:
        out_r.append(0)
    else:
        out_r.append(key_r.find(letter))

    if key_g.find(letter) == -1:
        out_g.append(0)
    else:
        out_g.append(key_g.find(letter))

    if key_b.find(letter) == -1:
        out_b.append(0)
    else:
        out_b.append(key_b.find(letter))
#print(out)

length = 460
mesl = len(input_mes)
image = np.zeros(shape = (length, length, 3), dtype = np.uint8)

'''
for i in range(length):
    if (i * length >= mesl):
        break
    for j in range(length):
        if(i * length + j == len(out_r)):
            break
        image[i,j,0] = int(out_r[i * length + j])
        image[i,j,1] = int(out_b[i * length + j])
        image[i,j,2] = int(out_g[i * length + j])
'''
for j in range(length):
        if(j == len(out_r)):
            break
        image[:,j,0] = int(out_r[j])
        image[:,j,1] = int(out_b[j])
        image[:,j,2] = int(out_g[j])

img = Image.fromarray(image)
img.save('message.bmp')
