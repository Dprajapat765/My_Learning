import cv2
import numpy as np

# sample img
img =  cv2.imread('demo.png', cv2.IMREAD_COLOR)
# draw a line in image
cv2.line(img, (0,0), (150,150), (255.0,0),15)
# draw a circle in image
cv2.circle(img, (100,65), 75, (0,0,255), -1)
# draw a rectangle
cv2.rectangle(img, (25,15), (200,150), (0,255,0), 5)

# draw a polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 5)

# write text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Output Image', (0,130), font, 1, (200,255,255), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


