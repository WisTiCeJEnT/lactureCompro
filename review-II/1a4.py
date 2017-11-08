positive = False
for i in range(1,42,2):
    if positive:
        print(i,end=' ')
        positive = False
    else:
        print('-'+str(i),end=' ')
        positive = True
print()
