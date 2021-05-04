import numpy as np
import cv2

pts1=np.array([(100,100,1),(400,100,1),(400,250,1),(100,250,1)], np.float32)  # 4개 좌표-동차 좌표

theta=45*np.pi/180    # 회전 각도-라디안 값
m=np.array([[np.cos(theta),-np.sin(theta),0],
           [np.sin(theta),np.cos(theta),0],
           [0,0,1]],np.float32)   # 회전 변환 행렬

delta=(pts1[2]-pts1[0])//2    # 시작 좌표와 종료 좌표 차분//2
center=pts1[0]+delta   #중심 좌표 계산

#평행 이동 행렬
t1=np.eye(3,dtype=np.float32)
t2=np.eye(3,dtype=np.float32)

# 증심 좌표 평행이동
t1[0][2] = center[0]  # 원점 센터로
t1[1][2] = center[1]
t2[0][2] = -center[0]   # 다시 원점으로
t2[1][2] = -center[1]

#행렬 곱 수행
m2=cv2.gemm(cv2.gemm(t1,m,1,None,1),t2,1,None,1) # 원점 센터로 이동*회전*다시 원점으로 이동

pts2=cv2.gemm(pts1,m2,1,None,1,flags=cv2.GEMM_2_T)

for i,(pt1,pt2) in enumerate(zip(pts1,pts2)):
    print("pts1[%d]=%s. pts2[%d]=%s"%(i,pt1,i,pt2))

image=np.full((400,500,3),255,np.uint8)
cv2.polylines(image,[np.int32(pts1[:,:2])],True,(0,255,0),2)
cv2.polylines(image,[np.int32(pts2[:,:2])],True,(255,0,0),3)
cv2.imshow("image",image)
cv2.waitKey(0)