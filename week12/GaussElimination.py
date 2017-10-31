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
    l = len(mat)
    for i in range(1,l):
        tmp = mat[i-1][i-1]
        tmp2 = mat[i-1][i]
        for j in range(len(mat[0])):
            mat[i][j] = mat[i][j] - mat[i-1][j]*tmp2/tmp
    return mat        

n = int(input())
m = int(input())
lis = inputlis()
lis = forwardE(lis)
printlis(lis)
