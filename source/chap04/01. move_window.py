import numpy as np
import cv2
# 회색창 만들고 윈도우 창 위치하기

image = np.zeros((200,400),np.uint8)    #0으로 채워진 200, 400 행렬을 만든다
image[:]=200   #image를 200으로 채운다(회색)


title1, title2='Position1','Position2'     # str할당
cv2.namedWindow(title1,cv2.WINDOW_AUTOSIZE)   # title1 윈도우 생성 및 크기 조정 autosize로
cv2.namedWindow(title2)  # 윈도우 생성-크기조정 defalt-normal
cv2.moveWindow(title1, 150, 150)  # 윈도우 해당 좌표로 움직이기
cv2.moveWindow(title2,400,50)

cv2.imshow(title1,image)   # title이름의 윈도우에 image라는 행렬을 영상으로 표시함
cv2.imshow(title2,image)
cv2.waitKey(0)   # 키 입력 대기
cv2.destroyAllWindows()  # 모든 창 파괴