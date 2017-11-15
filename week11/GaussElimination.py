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
        mat = mat[0:k] + pivoting(mat[k:len(mat)],k)
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

def printX(mat):
    for i in range(n):
        print("X{} = {:.5f}".format(i+1,mat[i][m-1]))

def pivoting(mat,col):
    if len(mat) == 1:
        return mat
    lisA = pivoting(mat[0:len(mat)//2],col)
    lisB = pivoting(mat[len(mat)//2 : len(mat)],col)
    #print("A:B",lisA,lisB)
    lisS = []
    while lisA or lisB:
        if not lisA:
            lisS.extend(lisB)
            break
        elif not lisB:
            lisS.extend(lisA)
            break
        if lisA[0][col]<lisB[0][col]:
            lisS.append(lisB.pop(0)) 
        else:
            lisS.append(lisA.pop(0)) 
    #print(lisS)
    return lisS
    
n = int(input())
m = n+1
lis = inputlis()
#
lis = forwardE(lis)
lis = backwardE(lis)
lis = getX(lis)
print()
printlis(lis)
printX(lis)
