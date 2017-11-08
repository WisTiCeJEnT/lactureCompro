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
    
def set0(r1,r2,s):
    for i in range(len(r1)):
        r2[i] = r2[i]*
def forwardE(mat):
    #set to 0 in row
    for i in range(m-1):
        t1 = mat[i][i]
        printlis(mat)
        #run the row
        for j in range(i+1,n):
            t2 = mat[j][i]
            #do in row
            for k in range(i,m):
                mat[j][k] = mat[j][k] - mat[j][k]*t1/t2
            
    return mat        

n = int(input())
m = int(input())
lis = inputlis()
lis = forwardE(lis)
print()
printlis(lis)
