def conv(n):
    dic = {'1':"one" , '2':"two" , '3':"three" , '4':"four" , '5':"five" , '6':"six" , '7':"seven" , '8':"eight" , '9':"nine" , '0':None}
    return dic[n]

n = input()
dit = {-1:"",0:"" ,1:"ty" , 2:"hundred" , 3:"thousand" , 6:"million"}
exl = {2,3,5}
exdit = {2:"twenty",3:"thirty",5:"fifty"}
i = len(n)
first = True
ans = ''
for c in n:
    j = i
    if not first:
        if(j%3!=0):
            j = (j)%3
        if(c in exl):
            ans = ans + exdit[c]
        else:
            ans = ans + dit[j]
        print(j)
    ans = ans + " " + conv(c)
    i-=1
    first = False
print(ans)
