def basedic(n):
    if(n<10):
        return str(n)
    elif(n<26):
        return chr(n-10+65)
def decton(num,n):
    if(num<n):
        return basedic(num)
    else:
        return decton(num//n,n) + basedic(num%n)
num = int(input("Convert : "))
n = int(input("To base : "))
print(decton(num,n))
