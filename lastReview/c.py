def det(mat):
    if len(mat) == 2:
        print(mat)
        print (mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0])
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

def replaced(mat,col):
    for i in range(len(mat)):
        mat[i][col] = k[i]
    print(mat)
    return mat

lis = [
    [1, 2],
    [3, 4]]
k = [5,11]
Det = det(lis)
x = det(replaced(lis,0))/Det
y = det(replaced(lis,1))/Det
print(x,y,Det)    
