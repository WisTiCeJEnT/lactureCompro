lis = ['c','b','a','v','a']
print lis
fi = lis.index('a')
ans = lis[fi:len(lis)].index('a')+(fi+1)

print(ans)
