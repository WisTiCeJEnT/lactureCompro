#Use string way
n = int(input())
s = '  '*(n-1)+'**'     #Create first line
for i in range(n):
    print(s)
    print(s)
    #Prepare next line
    s = s + '****'
    s = s[2:len(s)]
