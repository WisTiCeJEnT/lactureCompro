def crelis(x,n): #lis x to n
    lis = []
    count = x
    while count<=n:
        lis.append(count)
        count += x
    return lis
n = 45  #last num
lis3 = crelis(3,n)
lis5 = crelis(5,n)
for i in range(min(len(lis3),len(lis5))):
    print(lis3[i],end=' ')
    print(lis5[i],end=' ')
if len(lis5) > len(lis3):
    print(lis5[len(lis5)-1],end='')
elif len(lis5) < len(lis3):
    print(lis3[len(lis3)-1],end='')
print()
