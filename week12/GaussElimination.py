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
    
n = int(input())
m = int(input())
lis = inputlis()

printlis(lis)
