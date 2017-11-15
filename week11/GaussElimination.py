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
    for j in range(1,n):
        k = mat[j][0]/mat[0][0]
        for i in range(m):
            #mat[j][i] = mat[j][i]*k - mat[0][i]
            mat[j][i] = mat[j][i] - mat[0][i]*k
    return mat        

n = int(input())
m = int(input())
lis = inputlis()
lis = forwardE(lis)
print()
printlis(lis)
