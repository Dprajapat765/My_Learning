
import numpy as np
import cv2

img = cv2.imread('img1.png')
img2= cv2.imread('mainlogo.png')

# load image components
row,col, channel = img2.shape
roi = img[0:row,0:col]

# create the mask of the image
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# use a threshold
ret , mask  = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)





cv2.imshow('mask_image',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# adding two images with +
add =  img + img2

# using add 
add = cv2.add(img,img2)

# adding weight to each image 
add = cv2.addWeighted(img, 0.6, img2, 0.4, 0)
'''

# ROI - region of image
'''
img[55,55] = [255,255,255]

px = img[55,55]

img[100:150, 100:150] = [255,255,255]

watch_face = img[37:211, 107:294]
img[0:174, 0:187] = watch_face
'''

