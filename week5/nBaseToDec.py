base = int(input("From base : "))
num = int(input("Input : "))
ans = 0                 #Answer
i = 0                   
while(num>0):
    tmp = num%10            #Get the last digit of number
    ans += tmp * base**i    #Add every value of digit to Answer
    num = num//10           #Prepare num for next repeat
    i += 1                
print(ans)
