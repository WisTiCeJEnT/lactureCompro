sumOfPos = 0
sumOfNeg = 0
x = float(input("Enter a number: "))
while(x!=0):
    if(x<0):
        sumOfNeg += x
    else:
        sumOfPos += x
    x = float(input("Enter a number: "))
print("Sum of Postitive Number = %.2f"%(sumOfPos)) 
print("Sum of Negative Number = %.2f"%(sumOfNeg)) 
