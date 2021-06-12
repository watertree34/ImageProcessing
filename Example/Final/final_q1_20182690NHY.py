import numpy as np, cv2

def onThreshold(value):  # 이진화 수행
    
    huevalue = cv2.getTrackbarPos("Hue", "result")   # hue값 -트랙바로 받아옴
    satvalue = cv2.getTrackbarPos("Saturation", "result")  # saturation 값 -트랙바로 받아옴
    intensityvalue = cv2.getTrackbarPos("Intensity", "result")  # intensity 값 -트랙바로 받아옴

    # 이진화 수행 -  이미지 hsv값이 트랙바 값(임계값)보다 작으면 흰색, 크면 검정색
    _, hueResult = cv2.threshold(hue, huevalue, 255, cv2.THRESH_BINARY_INV)
    _, satResult = cv2.threshold(saturation, satvalue, 255, cv2.THRESH_BINARY_INV)
    _, intensityResult = cv2.threshold(intensity, intensityvalue, 255, cv2.THRESH_BINARY_INV)

    result = hueResult * satResult * intensityResult  # 세 값을 곱해주어 참이 되는 얼굴색 값을 찾을 것
    greenResult(result)
    cv2.imshow("result", result)   # 바이너리 이미지 창 출력



def greenResult(binResult):    # 해당 색 초록색으로 표현하기
    global frame
    greenFrame = frame
    blue, green, red = cv2.split(greenFrame)  #  컬러영상 채널분리
    cv2.add(green, 100, green)  # green채널에 100을 더한것을 green결과에 넣음
    greenFrame = cv2.merge([blue, green, red])  # 단일 채널 영상 다시 합성

    img_result = cv2.bitwise_and(greenFrame, greenFrame, mask=binResult)  # 바이너리 이미지를 마스크로 사용하여 초록 영상에서는 얼굴색만 나오게 함
    binResult = cv2.bitwise_not(binResult)  # 바이너리 이미지 반전시킴
    frame2=cv2.bitwise_and(frame, frame, mask=binResult)  # 얼굴색이 아닌부분만 원본영상으로 나오게 함
    img_result=cv2.add(frame2,img_result,img_result)   # 얼굴색이 나오는 초록영상과 얼굴색이 안나오는 원본 영상 합침
    
    cv2.imshow("img_result", img_result)  # 결과 이미지 창 출력



capture = cv2.VideoCapture(0)   # 카메라 연결

if capture.isOpened() == False: raise Exception("카메라 연결안됨")

th = [50, 50, 50]      # 트랙바로 선택할 범위 변수
cv2.namedWindow("result")
cv2.createTrackbar("Hue", "result", th[0], 255, onThreshold)  # 트랙바 생성
cv2.createTrackbar("Saturation", "result", th[1], 255, onThreshold)
cv2.createTrackbar("Intensity", "result", th[2], 255, onThreshold)

while True:
    ret, frame = capture.read()  # 카메라 읽기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 컬러 공간 HSV로 변환
    hue = np.copy(hsv_frame[:, :, 0])  # hue 행렬에 HSV색상 채널 복사
    saturation = np.copy(hsv_frame[:, :, 1])  # saturation 행렬에 HSV색상 채널 복사
    intensity = np.copy(hsv_frame[:, :, 2])  # intensity 행렬에 HSV색상 채널 복사

    cv2.imshow("frame", frame)
    onThreshold(th[0])  # 이진화 수행


capture.release()
cv2.destroyAllWindows()
