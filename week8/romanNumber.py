dic = {1:'I' , 5:'V' , 10:'X' , 50:'L' , 100:'C' , 500:'D' , 1000:'M'}
n = int(input())
ans = ""
while n>0:
    d = len(str(n))-1
    c = n//(10**d)
    n = n%(10**d)

    if c%5==4:  #4 or 9
        ans += dic[10**d]
        c += 1
        n += c*(10**d)
        continue
    while c>0:
        if c>=5:
            ans += dic[5*10**d]
            c -= 5
        else:
            ans += dic[10**d]
            c -= 1
print(ans)
