import numpy as np

list1=[1,2,3]
list2=[4,5.0,6]

a,b=np.array(list1), np.array(list2)

c=a+b
d=a-b
e=a*b
f=a/b
g=a*2
h=b*2

print('a자료형', type(a),type(a[0]))
print('b자료형', type(b),type(b[0]))
print('c자료형', type(c),type(c[0]))
print('g자료형', type(g),type(g[0]))
print(c,d,e)
print(f,g,h)