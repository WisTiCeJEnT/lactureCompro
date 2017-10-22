def fac(n):
    ans = n
    for i in range(1,n):
        ans *= i
    return ans
print(fac(int(input())))
