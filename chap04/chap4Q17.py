import cv2

capture=cv2.VideoCapture(0)
if capture.isOpened()==False: raise Exception("카메라 연결안됨")

fps=15   # fps
size=(640,480)   # 해상도
fourcc=cv2.VideoWriter_fourcc(*'DIVX')   # 동영상 코덱

writer=cv2.VideoWriter("./src/flip_test.avi",fourcc,fps,size) # 동영상 설정,개방

if writer.isOpened()==False: raise Exception("동영상 파일 개방 안됨")

while(1):

    ret,frame=capture.read()
    if not ret:
        break

    if cv2.waitKey(300)>=0:break

    frame=cv2.flip(frame,1)    # 좌우 뒤집기
    writer.write(frame)   # 프레임 동영상으로 저장
    cv2.imshow("myFrame",frame)

writer.release()
capture.release()