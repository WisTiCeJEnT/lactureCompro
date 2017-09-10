def conv(n):
    n = str(n)
    dic = {'1':"one" , '2':"two" , 
        '3':"three" , '4':"four" , 
        '5':"five" , '6':"six" , 
        '7':"seven" , '8':"eight" , 
        '9':"nine" , '0':""}
    return dic[n]
def hund(hh):
    exdit = {2:"twen",3:"thir",4:"for",5:"fif",
            6:"six",7:"seven",8:"eigh",9:"nine"}
    hans = ""
    hh = int(hh)
    if hh>=100:
        hans = conv(hh//100) + "hundred"
        hh = hh%100
    if hh>=20:
        if hh//10 in exdit:
            hans = hans + exdit[hh//10]
        else:
            hans = hans + conv(hh//10)
        hans += "ty"
        hh = hh%10
    if hh>=10:
        if hh == 10:
            hans = hans + "ten"
        elif hh == 11:
            hans = hans + "eleven"
        elif hh == 12:
            hans = hans + "twelve"
        else:
            hans = hans + exdit[hh%10] + "teen"
        hh = 0
    hans = hans + conv(hh)
    return hans
    
dit = {3:"thousand", 6:"million", 9:"billion"}
inp = input()
ans = ""
intAns = ""
D = 0
while inp:
    D += 3
    if(len(inp)>=3):
        h = inp[len(inp)-3:len(inp)]
        inp = inp[0:len(inp)-3]
    else:
        h = inp
        inp = ""
    ans = hund(h) + ans
    if inp:
        ans = dit[D] + " " + ans
    intAns = h + "," + intAns
print(intAns[0:len(intAns)-1])
print(ans)
"""
n = input()
exl = {2,3,5}
i = len(n)
first = True
ans = ''
for c in n:
    j = i
    if not first:
        if(j%3!=0):
            j = (j)%3
            if(int(c) in exl and j==1):
                ans = ans + exdit[j]
            else:
                ans = ans + dit[j]
        else:
            ans = ans + dit[j]
        print(j)
    ans = ans + " " + conv(c)
    i-=1
    first = False
print(ans)
"""
