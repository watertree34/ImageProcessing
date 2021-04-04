import cv2

cam = cv2.VideoCapture(0)
if not cam.isOpened():
  print ("Could not open cam")
  exit()

while(1):
    ret, frame = cam.read()

    if ret:

        ROI = frame[100:300, 200:300]    # 프레임의 시작y축:y+높이,시작x축:x+넓이 부분을 ROI로 지정

        blue, green, red = cv2.split(ROI)   #관심영역의 컬러영상 채널분리

        cv2.add(green, 50, green)    # green채널에 50을 더한것을 green결과에 넣음

        ROI = cv2.merge([blue, green, red])  # 관심영역의 단일 채널 영상합성
        frame[100:300, 200:300]=ROI    #프레임의 해당 영역에 ROI를 저장
        cv2.rectangle(frame, (200, 100, 100, 200), (0, 0, 255),3)   # 빨간색 사각형 테두리

        cv2.imshow('curFrame', frame)

    if cv2.waitKey(30) >= 0: break
cam.release()
cv2.destroyAllWindows()