from numpy.linalg import det as det
#import numpy
n = 4
A = []
for i in range(n):
    A.append(list(map(float,input().split())))
print(det(A))
