def plist(n):
    pls = []
    n += 1
    ls = list(range(n))
    for i in range(2,int(n**0.5)+1):
        if ls[i]:
            for dele in range(i+i,n,i):
                ls[dele] = False
    for i in range(2,n):
        if ls[i]:
            pls.append(i)
    return pls          #return list of prime
inp = int(input("Enter a positive integer greater than 1: "))
if inp>1:
    for i in plist(inp):
        while inp%i == 0:
            print(i)
            inp = inp/i
else:
    print("Input must be greater than 1")
