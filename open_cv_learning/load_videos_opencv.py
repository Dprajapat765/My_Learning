import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# lets record video with your camera
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output of the video with extentions and quality
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

while True:
	ret, frame =  cap.read()
	# load in gray 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()
