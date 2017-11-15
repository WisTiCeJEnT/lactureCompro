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
    k = mat[0][0]/mat[1][0]
    for i in range(m):
        mat[1][i] = mat[1][i]*k - mat[0][i]
    return mat        

n = int(input())
m = int(input())
lis = inputlis()
lis = forwardE(lis)
print()
printlis(lis)
