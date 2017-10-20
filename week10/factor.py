inp = int(input("Enter a positive integer greater than 1: "))
if inp>1:
    print("Prime factorization of {} is:".format(inp))
    i = 2
    b = False
    while inp>1:
        while inp%i!=0 and i<=inp:
            i += 1
            if i*i>inp:
                b = True
                break
#            print("try",i)
        if not b:
            print(i)
            inp = inp/i
        else:
            print(int(inp))
            break
else:
    print("Input must be greater than 1")
