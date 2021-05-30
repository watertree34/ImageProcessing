N=int(input())
k=int(input())

A=[[0]*N for _ in range(N)]

for i in range(0,N):
    for j in range(0, N):
        A[i][j]=i*j

B=sum(A,[])
B.sort()
print(B[k])