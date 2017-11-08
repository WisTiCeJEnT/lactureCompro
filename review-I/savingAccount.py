from math import pow
p = float(input("Principal = "))
r = float(input("Rate = "))
n = int(input("Years = "))
print("Amount = {:.5f}".format(p*pow((100+r)/100,n)))
