def printlis(tbl):
    for line in tbl:
        count = 0
        for _ in line:
            count += 1
            if count == m:
                print('|',end=' ')
            print(_,end=' ')
        print()

def inputlis():
    tmplis = []
    for i in range(n):
        tmplis.append(list(map(float,input().split())))
    return tmplis
    
def forwardE(mat):
    for k in range(n):
        for j in range(k+1,n):
            c = mat[j][k]/mat[k][k]
            for i in range(m):
                mat[j][i] = mat[j][i] - mat[k][i]*c
    return mat        

def backwardE(mat):
    for k in range(n-1,-1,-1):
        for j in range(k-1,-1,-1):
            c = mat[j][k]/mat[k][k]
            for i in range(m):
                mat[j][i] = mat[j][i] - mat[k][i]*c
    return mat        
    
def getX(mat):
    for i in range(n):
        mat[i][m-1] /= mat[i][i]
        mat[i][i] = 1
    return mat
n = int(input())
m = int(input())
lis = inputlis()
lis = forwardE(lis)
lis = backwardE(lis)
lis = getX(lis)
print()
printlis(lis)
