c = int(input())
mode = input()
if mode == 'F':
    print("{:.2f}".format(c/5*9+32))
elif mode == 'R':
    print("{:.2f}".format(c/5*4))
elif mode == 'K':
    print("{:.2f}".format(c+273))
