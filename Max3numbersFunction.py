# Python function to find the Max of three numbers
def maximum(x,y,z):
    result=max(x,y,z)
    return result
#user input
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))
#print result
print("x=",x,"y=",y,"z=",z)
print("the max  is;", maximum(x,y,z))
#end of program