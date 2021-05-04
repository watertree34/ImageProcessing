import cv2
import numpy as np

# 이미지 파일 읽기
add_image1 = cv2.imread("images/01.jpg")
add_image2 = cv2.imread("images/02.jpg")
add_image3 = cv2.imread("images/03.jpg")

if add_image1 is None or add_image2 is None or add_image3 is None:raise Exception("영상 파일 읽기 오류")

title="add image"

def add(value):  # 트랙바 움직일 때
    global title
    weight_image1 = cv2.getTrackbarPos("image1", title)
    weight_image2 = cv2.getTrackbarPos("image2", title)
    weight_image3 = cv2.getTrackbarPos("image3", title)
    # 영상 비율에 따른 더하기
    result = cv2.addWeighted(add_image1, weight_image1 / 100, add_image2, weight_image2 / 100, 0)
    result = cv2.addWeighted(result, 1, add_image3, weight_image3 / 100, 0)

    cv2.imshow(title, np.hstack([add_image1, add_image2, add_image3, result]))

cv2.namedWindow(title)

cv2.createTrackbar("image1",title, 0, 100, add)
cv2.createTrackbar("image2", title, 0, 100, add)
cv2.createTrackbar("image3", title, 0, 100, add)

cv2.waitKey(0)
cv2.destroyAllWindows()

