import numpy as np
import cv2

olive, violet, brown= (128,128,0),(221,160,221), (42,42,165)
pt1, pt2=(50,230),(50,310)

image=np.zeros((350,500,3),np.uint8)
image.fill(255)

cv2.putText(image,'SIMPLEX',(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,brown)
cv2.putText(image,'SIMPLEX',(50,50),cv2.FONT_HERSHEY_SIMPLEX,3, olive)
cv2.putText(image,'SIMPLEX',(50,50),cv2.FONT_HERSHEY_SIMPLEX,3, violet)
fontFace=cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
cv2.putText(image,'ITALIC',pt2, fontFace, 4, violet)

cv2.imshow('Put Text', image)
cv2.waitKey(0)