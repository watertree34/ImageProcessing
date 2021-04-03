import numpy as np
import cv2


#키보드 이벤트 제어-키를 입력하면 콘솔창에 뭐 입력했는지 뜨게 하기
switch_case={
    ord('a'): " a키 입력",
    ord('b'):"b키 입력",
    0X41:"A키 입력",
    int('0x42',16): "B키 입력",
    2424832:"왼쪽 화살표키 입력"

}

image = np.ones((200,300),np.float64)
cv2.namedWindow('keyboard event')
cv2.imshow("keyboard event",image)

while True:
    key=cv2.waitKeyEx(100)
    if key==27:break

    try:
        result=switch_case[key]
        print(result)
    except KeyError:
        result=-1
cv2.destroyAllWindows()
