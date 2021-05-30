import numpy as np, cv2

def draw_rect(img):  # 사각형 4개 그리기
    rois = [(p - small, small * 2) for p in pts1]
    for (x, y), (w, h) in np.int32(rois):
        roi = img[y:y + h, x:x + w]  # 좌표 사각형 범위 가져오기
        val = np.full(roi.shape, 80, np.uint8)  # 컬러(3차원) 행렬 생성		cv2.add(roi, val, roi)     	# 관심영역 밝기 증가
        cv2.add(roi, val, roi)
        cv2.rectangle(img, (x, y, w, h), (0, 255, 0), 1)
    cv2.polylines(img, [pts1.astype(int)], True, (0, 255, 0), 1)  # pts는 numpy 배열
    cv2.imshow("select rect", img)


def warp(img):  
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)  # 원근 변환 행렬
    dst = cv2.warpPerspective(img, perspect_mat, (350, 400), cv2.INTER_CUBIC)  # 영상에 적용
    cv2.imshow("perspective transform", dst)

def contain_pts(p, p1, p2):   # 좌표가 사각형 안에 있는지 판단
    return p1[0] <= p[0] < p2[0] and p1[1] <= p[1] < p2[1]

def onMouse(event, x, y, flags, param):
    global check
    if event == cv2.EVENT_LBUTTONDOWN:   # 마우스 클릭했을 때 클릭 좌표가 사각형 안에 있는지 확인
        for i, p in enumerate(pts1):    # p는 pts1 인덱스 순서대로
            p1, p2 = p - small, p + small  # p점에서 우상단, 좌하단 좌표생성
            if contain_pts((x, y), p1, p2): check = i    # 마우스가 좌표안에 있으면 check 갱신

    if event == cv2.EVENT_LBUTTONUP: check = -1  # 클릭 끝나면 좌표 번호 초기화

    if check >= 0:  # 좌표 사각형 선택 시
        pts1[check] = (x, y)


capture = cv2.VideoCapture(0)   # 카메라 연결

if capture.isOpened() == False: raise Exception("카메라 연결안됨")

pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)]) # 입력영상 4개 좌표
pts2 = np.float32([(0, 0), (400, 0), (400, 350), (0, 350)])  # 목적영상 4개 좌표
small = np.array((12, 12))  # 좌표 사각형 크기
check = -1  # 선택 좌표 사각형 번호 초기화

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    draw_rect(np.copy(frame))
    warp(np.copy(frame))
    cv2.setMouseCallback("select rect", onMouse)

capture.release()
cv2.destroyAllWindows()