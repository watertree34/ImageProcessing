import numpy as np
import cv2
# 마우스 이벤트 사용하기  
def onMouse(event,x,y,flags,param):    # 콜백함수
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽버튼 누르기")
    elif event==cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽버튼 누르기")
    elif event==cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event==cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")

image=np.full((200,300),255,np.uint8)   # 초기영상 생성

title1,title2="Mouse Event1","Mouse Event2"  #윈도우 이름
cv2.imshow(title1,image)
cv2.imshow(title2,image)

cv2.setMouseCallback(title1,onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
