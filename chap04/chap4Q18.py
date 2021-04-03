import numpy as np
import cv2

red,blue,white=(0,0,255),(255,0,0),(255,255,255)  # 빨강, 파랑 색 지정

image=np.full((400,600,3),white,np.uint8)

ptBig,ptSmallR,ptSmallB=(300,200), (250,200),(350,200)   # 큰 반원 반지름, 작은 빨간 반원 반지름, 작은 파란 반원 반지름

bigSize=(100,100)  # 큰 반원들 x,y반지름
smallSize=(50,50)  # 작은 반원들 x,y반지름

cv2.ellipse(image,ptBig,bigSize,180,0,180,red,-1)  # 큰 빨간 반원
cv2.ellipse(image,ptBig,bigSize,0,0,180,blue,-1)   # 큰 파란 반원
cv2.ellipse(image,ptSmallR,smallSize,0,0,180,red,-1)  # 작은 빨간 반원
cv2.ellipse(image,ptSmallB,smallSize,180,0,180,blue,-1)   # 작은 파란 반원

cv2.imshow("image",image)
cv2.waitKey(0)
