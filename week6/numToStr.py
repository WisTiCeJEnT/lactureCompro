def conv(n):
    dic = {'1':"one" , '2':"two" , '3':"three" , '4':"four" , '5':"five" , '6':"six" , '7':"seven" , '8':"eight" , '9':"nine" , '0':None}
    return dic[n]

n = input()
dit = {1:"",0:"" ,2:"ty" , 3:"hundred" , 4:"thousand"}
i = len(n)+1
first = True
ans = ''
for c in n:
    j = i
    if not first:
        if((j-1)%3!=0):
            j = j%3
        ans = ans + dit[j]
        print(j)
    ans = ans + conv(c)
    i-=1
    first = False
print(ans)
