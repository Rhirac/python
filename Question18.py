#Quesion18

import matplotlib.pyplot as plt
import numpy as np

img = np.ones( (30,30,3) )
img[:,:10,0:2] = 0
img[:,20:30,0:2] = 0
img[20:30,10:20,0:2] = 0
plt.imsave('logo.png', img)