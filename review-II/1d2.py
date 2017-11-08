ans = 3
for i in range(2,201,2):
    if i%4==0:
        ans -= 4/(i*(i+1)*(i+2))
    else:
        ans += 4/(i*(i+1)*(i+2))
print(ans)
