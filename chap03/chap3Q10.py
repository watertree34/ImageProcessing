import numpy as np
import collections

ndarray = np.random.randint(0,50,500)  # 0~50 사이의 랜덤값 500개 생성
print(ndarray)

counter = collections.Counter(ndarray)  # 숫자들의 횟수 세주기
#print(counter)

a=list(counter.items())     # counter 딕셔너리를 튜플 리스트로 만들기
a.sort(key=lambda x: x[1])  # 중복횟수를 기준으로 오름차순 정렬

print("가장 중복이 많이 나온 원소 3개의 (원소 값, 중복횟수): ",a[:-4:-1])   # 끝에서 3개 출력

