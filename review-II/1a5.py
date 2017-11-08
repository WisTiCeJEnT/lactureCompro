#Fibo
a = 1
b = 1
c = -1
print("0 1 1 ",end='')
while c<144:
    c = a + b
    a = b
    b = c
    print(c,end=' ')
print()
