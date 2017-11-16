def leap(y):
    ans = False
    if y%4 == 0:
        if y%100 != 0:
            ans = True
        else:
            if y%400 == 0:
                ans = True
    return ans
M = int(input("M = "))
Y = int(input("Y = "))
m = 1
y = 1970
kom = [1,3,5,7,8,10,12]
date = 4
while y!=Y:
    if leap(y):
        date += 366
    else:
        date += 365
    y += 1
dim = 31
while m!=M+1:
    if m in kom:
        dim = 31
    elif m != 2:
        dim = 30
    else:
        if leap(y):
            dim = 29
        else:
            dim = 28
    if m == M:
        break
    date += dim
    m += 1
date %= 7
#print(dim,date)
print("Sun Mon Tue Wed Thu Fri Sat")
print("    "*date,end='')
i = 1
while i <= dim:
    if date < 7:
        print("{:3}".format(i),end=' ')
        i += 1
        date += 1
    else:
        date = 0
        print()
print()
