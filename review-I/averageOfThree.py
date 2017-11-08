#This task from other  section of 10204111 class
#PY-04-Subroutine2
def input3num():
    a = int(input())
    b = int(input())
    c = int(input())
    return a,b,c
def avr(a,b,c):
    return (a+b+c)/3
x,y,z = input3num()   #must have 3 var to receive else "ValueError: too many values to unpack"
print(avr(x,y,z))
