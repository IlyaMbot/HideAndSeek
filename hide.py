import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


def plotting_image(image):
    px = 1/plt.rcParams['figure.dpi'] 
    
    fig = plt.figure() 
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    imgplot = plt.imshow(image,  interpolation='none')    	
    plt.savefig('./The_model.png', transparent=False, dpi=200, bbox_inches='tight', pad_inches=0)
    #plt.show()

filename1 = 'mes.jpeg'
#filename1 = 'my.png'
filename2 = "message.bmp"
img1 = mpimg.imread(filename1)
img2 = mpimg.imread(filename2)

imgg = np.zeros_like(img1)

for i in range(3):
    imgg[:,:,i] = (img1[:,:,i] + img2[:,:,i])
'''

img2 = img2/50

imgg[:,:,0] = (img1[:,:,1] * img2[:,:,2])
imgg[:,:,1] = (img1[:,:,2] * img2[:,:,0])
imgg[:,:,2] = (img1[:,:,0] * img2[:,:,1])

'''
img = Image.fromarray(imgg)
img.save('hidden.png')

imgplot = plt.imshow(imgg)
plt.show()
'''
plotting_image(imgg)
'''