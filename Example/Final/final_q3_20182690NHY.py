import cv2 as cv

def draw_ball_location(frame, locations, nowColor):    # 선 그리기 함수

    for i in range(len(locations) - 1):

        if locations[0] is None or locations[1] is None:
            continue

        cv.line(frame, tuple(locations[i]), tuple(locations[i + 1]), nowColor[i], 3)  # 이전 위치에서 현재 위치로 선 그리기

    return frame


color=(0,255,255)  # 선 색깔
dirValue = 300  # 방향 인식 임계값
dirResult = ""  # 방향
def recogDirColor(locEnd,locStart):   # 제스쳐 방향에 따라 색깔 바꾸기 함수
    global color, dirValue,dirResult


    xlen = locEnd[0] - locStart[0]  # x축 나중위치-현재위치 이동 거리
    ylen = locEnd[1] - locStart[1]  # y축 나중위치-현재위치 이동 거리

    if abs(xlen) > dirValue:   # x축이 임계값보다 많이 이동했다면
        if xlen < 0:  # 부호에 따라 왼쪽, 오른쪽 판단
            dirResult = "왼쪽"
            color=(0,0,255)  # 빨강
            print(dirResult)
        else:
            dirResult = "오른쪽"
            color=(255,0,0)  # 파랑
            print(dirResult)

    elif abs(ylen)>dirValue: # y축이 임계값보다 많이 이동했다면
        if ylen > 0:    # 부호에 따라 위쪽, 아래쪽 판단
            dirResult = "아래쪽"  
            color = (0, 255, 0)  # 초록
            print(dirResult)
        else:
            dirResult = "위쪽"
            color = (0, 255, 255)  # 노랑
            print(dirResult)


def drawUI():   # ui그리기 함수
    global isDraw
    cv.putText(frame, "Gesture Change Color(key c):          / Now Color: ", (0, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (150, 100, 50), 2)
    cv.putText(frame, str(isColorChange), (250, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5,(0, 50, 150), 2)
    cv.rectangle(frame, (430,10),(440,20),color,cv.FILLED)
    cv.putText(frame, "--> Left : Red, Right : Blue, Up : Yellow, Down : Green", (0, 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (150, 100, 50), 2)
    cv.putText(frame, "Draw Enable(key v) : ", (0, 60), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 200), 2)
    cv.putText(frame, str(isDraw), (170, 60), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 150), 2)
    cv.putText(frame, "Clear : space bar", (0, 80), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100, 150, 100), 2)
    cv.putText(frame,"Exit : esc",(0,100),cv.FONT_HERSHEY_SIMPLEX,0.5,(10,10,10),2)





cap = cv.VideoCapture(0)  # 카메라 연결

list_blue_location = []   # 선 그리기를 할 때 사용할 파란물체 위치 리스트
list_dir_location = []   # 동작 방향인식을 할 때 사용할 파란물체 위치 리스트
list_nowColor = []   # 현재 선의 색깔 리스트

history_blue_locations = []  # 이전에 그린 위치 리스트
history_nowColor=[]  # 이전에 그린 선 색깔 리스트

isDraw = True
isColorChange = False

while True:

    ret, frame = cap.read()   #카메라 읽기
    if not ret: break
    frame = cv.flip(frame, 1)  # 좌우 반전

    img_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)   # hsv로 바꾸기

    hue_blue = 100  # 인식할 물체 blue색 범위 지정
    lower_blue = (hue_blue -30, 150, 0)
    upper_blue = (hue_blue + 30, 255, 255)
    img_mask = cv.inRange(img_hsv, lower_blue, upper_blue)   # 파란색 검출 마스크

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  #5*5커널
    img_mask = cv.morphologyEx(img_mask, cv.MORPH_DILATE, kernel, iterations=3) # 모폴로지 연산 Cv.MorphologyEx(원본, 결과, 임시, 요소, 연산 방법, 반복횟수)

    nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(img_mask) # 레이블 갯수, 레이블 영역에 대한 통계 정보 행렬, 중심위치도 함께 반환

    max = -1
    max_index = -1


    for i in range(nlabels):

        if i < 1:
            continue

        # 파란색 객체가 검출되면
        area = stats[i, cv.CC_STAT_AREA]   # stats( 각 레이블 영역에 대한 통계 정보 행렬 )을 이용해 면적 구함

        if area > max:   # 화면 속 다양한 파란 물체 중 가장 면적이 큰 파란색 물체를 펜으로 인식
            max = area
            max_index = i

    if max_index != -1: # 화면에 파란색 물체가 있으면

        center_x = int(centroids[max_index, 0])     # 물체의 위치와 가로 세로 정보 저장
        center_y = int(centroids[max_index, 1])
        left = stats[max_index, cv.CC_STAT_LEFT]
        top = stats[max_index, cv.CC_STAT_TOP]
        width = stats[max_index, cv.CC_STAT_WIDTH]
        height = stats[max_index, cv.CC_STAT_HEIGHT]

        cv.rectangle(frame, (left, top), (left + width, top + height), (0, 0, 255), 5) # 물체 겉에 사각형 그리기
        cv.circle(frame, (center_x, center_y), 10, color, -1)  # 물체 중심에 원 그리기

        if isDraw: # 그리기 상태면 위치, 색 리스트에 현재 위치,선 색 추가
            list_blue_location.append((center_x, center_y))
            list_nowColor.append(color)

        else:  # 아니면 history 리스트에 현재 위치,선 색 널고 현재 위치,선 색 초기화
            history_blue_locations.append(list_blue_location.copy())
            history_nowColor.append(list_nowColor.copy())
            list_blue_location.clear()
            list_nowColor.clear()

        if (isColorChange):  # 색 바꾸기 상태면 list_dir_location에 물체위치 추가 후 색바꾸기 함수 호출
            list_dir_location.append((center_x, center_y))
            if(len(list_dir_location)>2):
                recogDirColor(list_dir_location[-1], list_dir_location[-2])


    frame = draw_ball_location(frame, list_blue_location, list_nowColor)  # 그리기 함수 호출

    for i in range(len(history_blue_locations)):   # 그린 기록있으면
        frame = draw_ball_location(frame, history_blue_locations[i], history_nowColor[i])   # 그리기 함수 호출



    drawUI()  # UI그리기

    cv.imshow('Blue', img_mask)
    cv.imshow('Result', frame)

    key = cv.waitKey(1)
    if key == 27:  # esc
        break
    elif key == 32:  # space bar
        list_blue_location.clear()
        list_dir_location.clear()
        list_nowColor.clear()
        history_blue_locations.clear()
        history_nowColor.clear()
    elif key == ord('v'):
        isDraw = not isDraw
    elif key == ord('c'):
        isColorChange = not isColorChange

cap.release()
cv.destroyAllWindows()