import math
x = int(input("X = "))
y = int(input("Y = "))
print("Seta = {:.2f}".format(math.degrees(math.atan(y/x))))
print("distance = {:.2f}".format(math.sqrt(x*x+y*y)))
