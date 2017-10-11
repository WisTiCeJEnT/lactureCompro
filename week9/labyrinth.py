#n,m = map(int,input().split())
#tbl = [[['']*m]*n]

def printTbl():
    for i in tbl:
        print(i)
def find(x,y,path):
    #if tbl[x][y] == 'e':
    print(path)
    global tbl
    tbl[x][y] = '*'
    if x>0:
        if tbl[x-1][y] == ' ':
            find(x-1,y,path+'U')
    if y>0:
        if tbl[x][y-1] == ' ':
            find(x,y-1,path+'L')
    if x<l-1:
        if tbl[x+1][y] == ' ':
            find(x+1,y,path+'D')
    if y<len(tbl[0])-1:
        if tbl[x][y+1] == ' ':
            find(x,y+1,path+'R')
tbl = []
l = int(input("How many line : "))
for i in range(l):
    tbl.append(list(input()))
printTbl()
find(0,0,"")
print()
printTbl()
