#n,m = map(int,input().split())
#tbl = [[['']*m]*n]

def printTbl():
    for i in tbl:
        print(i)
def find(x,y,path):
    if tbl[x][y] == 'e':
        print(path)
    tbl[x][y] = '*'
    if x>0 and tbl[x-1][y] == ' ':
        find(x-1,y,path+'L')
    if y>0 and tbl[x][y-1] == ' ':
        find(x,y-1,path+'U')
    if x<len(tbl[0]) and tbl[x-1][y] == ' ':
        find(x+1,y,path+'R')
    if y<l and tbl[x-1][y] == ' ':
        find(x,y+1,path+'D')
tbl = []
l = int(input("How many line : "))
for i in range(l):
    tbl.append(list(input()))
printTbl()
find(0,0,"")
printTbl()
