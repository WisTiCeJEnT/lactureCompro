map = [[' ',' ',' ','*',' ',' ',' '],
       ['*','*',' ','*',' ','*',' '],
       [' ',' ',' ',' ',' ',' ',' '],
       [' ','*','*','*','*','*',' '],
       [' ',' ',' ',' ',' ',' ','e']]
def findPath(x, y, path) : 
    global map
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]) : return 
    if map[x][y] == 'e' : print(f'Found path: {path}')
    if map[x][y] != ' ' : return
    map[x][y] = 'v'
    findPath(x, y-1, path+'L') 
    findPath(x, y+1, path+'R') 
    findPath(x-1, y, path+'U') 
    findPath(x+1, y, path+'D') 
    map[x][y] = ' '
findPath(0, 0, '')
