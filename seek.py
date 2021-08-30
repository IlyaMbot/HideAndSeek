import numpy as np
import matplotlib.image as mpimg


key_r = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_b = " abcdefghijklmnopqrstuvwxyz"
key_g = " 1234567890!?.,:;'-+"

filename1 = 'mes.jpeg'
filename2 = "hidden.png"

img1 = mpimg.imread(filename1)
img2 = mpimg.imread(filename2)

res = np.zeros(shape = (len(img1), len(img1), 3), dtype = np.uint8)

for i in range(3):
    res[:,:,i] = img2[:,:,i]*255 - img1[:,:,i]

for i in res[0]:
    print(key_r[i[0]], key_b[i[1]], key_g[i[2]])