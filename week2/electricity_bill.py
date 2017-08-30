A = [5,10,65,120,200]
unit = int(input("Unit = "))
cost = 0
j = 0
for i in A:
    if(unit>=i):
        cost += i*j
        unit -= i
    else:
        cost += unit * j
        unit = 0
    j += 0.5
print(cost)
