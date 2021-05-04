import cv2
import numpy as np


click = False
x0=0
y0=0

def rect(event, x, y, flags, param):  #관심영역 그리기 함수
    global x0, y0, click

    if event == cv2.EVENT_LBUTTONDOWN:  # 좌클릭 눌렀을 때
        click = True
        x0, y0 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # 드래그 할 때
        if click == True:

            if y0<y:
                roi = frame2[y0 : y, x0: x]
                image[y0 : y, x0: x] = roi
            else:
                roi = frame2[y: y0, x: x0]
                image[y: y0, x: x0] = roi

    elif event == cv2.EVENT_LBUTTONUP:  # 버튼에서 손가락을 뗐을 때
        click = False
        cv2.rectangle(image, (x0, y0), (x, y), (0, 0, 255), 3)



Cap = cv2.VideoCapture(0)

k = Cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
v = Cap.get(cv2.CAP_PROP_FRAME_WIDTH)
if Cap.isOpened() is None:
    raise Exception("카메라 연결 안됨")


title = "drag roi"
image = np.full((300, 400, 3), (0,0,0), np.uint8)
while True:
    ret, frame = Cap.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    frame2 = cv2.resize(frame, (400, 300), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
    cv2.setMouseCallback(title, rect)
    cv2.imshow(title, image)


