import numpy as np
import cv2

orange, blue, white=(0,165,255), (255,0,0), (255,255,255)
image=np.full((300,700,3),white,np.uint8)

pt1, pt2=(180,150),(550,150)
size=(120,60)    #타원 반지름의 크기(x축, y축)

cv2.circle(image,pt1,1,0,2)
cv2.circle(image,pt2,1,0,2)
#ellipse( 그릴 대상, 원의 중심좌표, 타원의 절반크기(x,y), 타원의 각도(3시 방향이 0도), 호의 시작각도, 호의 종료각도, 선의 색상, 선 두께)
cv2.ellipse(image,pt1,size,0,0,360,blue,1)
cv2.ellipse(image,pt2,size,90,0,360,blue,1)
cv2.ellipse(image,pt1,size,0,30,270,orange,4)
cv2.ellipse(image,pt2,size,90,-45,90, orange,4)

cv2.imshow("문자열", image)
cv2.waitKey()