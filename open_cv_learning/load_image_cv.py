# importing necessary modules
import numpy as np
import matplotlib.pyplot as plt
import cv2

# load an image 
# READING AN IMAGE IN DIFFERENT MODE
'''
1. IMREAD_GRAYSCALE (in number 0)
2. IMREAD_COLOR ( in number 1)
3. IMREAD_UNCHANGED ( in number -1)
'''
img = cv2.imread("demo.png",0)

# show the image
cv2.imshow("image", img)
# close the image when any key pressed
cv2.waitKey(0)
# destroy all windows after pressing key
cv2.destroyAllWindows()
