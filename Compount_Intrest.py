#program to calculate compound interest
#formula A= P(1 + R/100)t
#Function
def CompoundInterest(p,r,t):
    CompInt = p *(pow((1 + r / 100),t))
    return CompInt
 
 #prompt user input for principle,rate amd time
print("INPUT VALUES")
p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
t = float(input("Enter the time in years: "))
 
 #calculating for amount and interest
amount=CompoundInterest(p,r,t)
interest =amount - p
print("Compound amount=;" , amount)
print("Compound interest =;" , interest)

#end of program