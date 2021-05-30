import cv2

def DetectEdge(low, high):
	rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)         	# 가우시안 블러링
	rep_edge = cv2.Canny(rep_edge, low, high, 5)						# 캐니 에지 검출
	cv2.imshow("canny edge", rep_edge)

def LowValue(a):
    global low
    low=a

def HighValue(b):
    global high
    high=b

capture = cv2.VideoCapture(0)   # 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결안됨")

low = 50
high = 150

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    rep_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
    cv2.namedWindow("canny edge", cv2.WINDOW_AUTOSIZE)  # 윈도우 생성
    cv2.createTrackbar("low", "canny edge", low, 250, LowValue)  # 콜백 함수 등록
    cv2.createTrackbar("high", "canny edge", high, 250, HighValue)  # 콜백 함수 등록
    cv2.imshow("frame", frame)
    DetectEdge(low, high)

capture.release()
cv2.destroyAllWindows()