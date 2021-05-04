import cv2
import numpy as np

data=[3,6,3,   -5,6,1,   2,-3,5]
m1=np.array(data,np.float32).reshape(3,3)
m2=np.array([2, 10, 28],np.float32)
dst=np.array((0,0,0),np.float32)
cv2.solve(m1,m2,dst)  #연립 방정식 풀기

print(dst)