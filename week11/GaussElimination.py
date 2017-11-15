def printlis(tbl):
    for line in tbl:
        for _ in line:
            print(_,end=' ')
        print()

def inputlis():
    tmplis = []
    for i in range(n):
        tmplis.append(list(map(int,input().split())))
    return tmplis
    
def forwardE(mat):
    for k in range(n):
        for j in range(k+1,n):
            c = mat[j][k]/mat[k][k]
            for i in range(m):
                mat[j][i] = mat[j][i] - mat[k][i]*c
    return mat        

n = int(input())
m = int(input())
lis = inputlis()
lis = forwardE(lis)
print()
printlis(lis)
