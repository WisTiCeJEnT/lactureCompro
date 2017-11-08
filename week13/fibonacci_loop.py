n = int(input())
a = 1
b = 1
print("0\n1\n1")
for i in range(n-2):
    a,b = b,a+b
    print(b)
