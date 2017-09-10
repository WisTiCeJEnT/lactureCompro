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

#dit call by 10^n
dit = { 3:"Thousand", 6:"Million", 9:"Billion", 12:"Trillion", 
        15:"Quadrillion", 18:"Quintillion", 21:"Sextillion", 24:"Septillion",       27:"Octillion", 30:"Nonillion", 33:"Decillion"}
inp = str(int(input()))     #For convert 0010 -> 10
ans = ""
intAns = ""
D = 0
if inp == "0":
    ans = "Just Zero"
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
