s = 400
an = 0 #Starter
lastA = 1 #a1 
while abs((lastA+s/lastA)/2-lastA) >= 10**(-8):
    an = (lastA+s/lastA)/2
    lastA = an
print(an)
