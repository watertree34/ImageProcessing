import cv2

image=cv2.imread("./src/norway.jpg",cv2.IMREAD_GRAYSCALE)

if image is None: raise Exception("영상 파일 읽기 에러")

params_jpg=(cv2.IMWRITE_JPEG_QUALITY,100)  # jpg화질
params_png=[cv2.IMWRITE_PNG_COMPRESSION,9]  #png압축레벨


cv2.imwrite("./src/test.jpg",image,params_jpg)
cv2.imwrite("./src/test.png",image,params_png)

cv2.imshow("image",image)
cv2.waitKey(0)

