##################################################
## Problem: mygauss.py
## Std: std05
## Name: Wattanai Sathuphan
## StudentId: 6010500117
##################################################

#---------------------------------------------------
def clearScreen():
    print(chr(27) + "[2J")

def readMat(filename, show=''):
    res = []
    inf = open(filename, 'r')
    for line in inf.readlines():
        tmp = []
        for col in line.split():
            tmp.append(float(col))
        res.append(tmp)
    if show == '':
        show = filename
    print(show)
    printMat(res, True)
    return res

def printMat(a, pretty=True):
    for row in a:
        for col in row:
            if pretty:
                print("%12.5f"%(col), end=' ')
            else:
                print("%12.5e"%(col), end=' ')
        print()
    print()

#---------------------------------------------------
# Begin your code here
#---------------------------------------------------
def plus(a,b):
    c = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        c.append(row)
    return c

def minus(a,b):
    c = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]-b[i][j])
        c.append(row)
    return c

def multi(a,b):
    c = []
    for i in range(len(b[0])):
        row = []
        for j in range(len(a)):
                tmp = 0
                for k in range(len(b)):
                    tmp += a[i][k] * b[k][j]
                row.append(tmp)
        c.append(row)
    return c 

def copyOf(x):
    newX = []
    for row in x:
        tmp = []
        for _ in row:
            tmp.append(_)
        newX.append(tmp)
    return newX
def inverse(mat):
    mat = copyOf(mat)
    ans = [[1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]]
    I = copyOf(ans)
    #ForwardE
    n = len(mat)
    m = len(mat[0])
    for k in range(n):
        for j in range(k+1,n):
            c = mat[j][k]/mat[k][k]
            for i in range(m):
                mat[j][i] = mat[j][i] - mat[k][i]*c
                ans[j][i] = ans[j][i] - ans[k][i]*c
            #print("=========")
            #printMat(ans)
    #BackwardE
    for k in range(n-1,-1,-1):
        for j in range(k-1,-1,-1):
            c = mat[j][k]/mat[k][k]
            for i in range(m):
                mat[j][i] = mat[j][i] - mat[k][i]*c
                ans[j][i] = ans[j][i] - ans[k][i]*c
    #clearX
    for i in range(n):
        c = mat[i][i]
        mat[i][i] = 1
        for j in range(m):
            ans[i][j] /= c
    return ans

#---------------------------------------------------
# Complete your main program from here
#---------------------------------------------------
clearScreen()
A = readMat('/tmp/gaussA/input_matrixA.txt', 'A=')
B = readMat('/tmp/gaussA/input_matrixB.txt', 'B=')
C = readMat('/tmp/gaussA/input_matrixC.txt', 'C=')

print("When X' is inverse matrix of X,")
print(" then AB + CA is")
res1 = plus(multi(A,B),multi(C,A))
printMat(res1)
print(" and (AB' + CA')' is")
res2 = inverse(plus(multi(A,inverse(B)), multi(C,inverse(A))))
printMat(res2)
print(" and (AB' - CA')(AB' - CA')' is")
ABCA = minus( multi(A,inverse(B)), multi(C,inverse(A)))
res3 = multi( ABCA , inverse(ABCA) )
printMat(res3, False)
printMat(res3, True)

