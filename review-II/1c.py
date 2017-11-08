import math
def f(n):
    return 15 + 10*math.sin(n/10)

print("  n | f(n)")
print("----+-------------------------------------------------")
for n in range(0,81,5):
    spaces = " " * round(f(n))
    print(f" {n:2} | {spaces}*")
