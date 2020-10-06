#Question 21

import matplotlib.pyplot as plt
import numpy as np

num = int(input('Enter size: '))
output = input('Enter output file name: ')
img = np.ones( (num,num,3) ) 
img[::2,:,0:3:2] = 0
plt.imsave(output, img)