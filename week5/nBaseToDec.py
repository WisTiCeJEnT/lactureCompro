base = int(input("From base : "))
num = int(input("Input : "))
ans = 0
i=0
while(num>0):
    tmp = num%10
    ans = ans + tmp * base**i
    num = num//10
    i += 1
print(ans)
