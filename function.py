#question 1: Write a function to find the area of a circle. The value of radius should be entered by user.
def circle(r,pi=3.142):
    return pi*r*r
radius = int(input("enter the value of radius ="))
print("Area of a circle=",circle(radius))
# question 2 :find the power of the given number ask value from user.
def power(a,b):
    return a**b
num1=int(input("enter the value of number1 ="))
num2=int(input("enter the value of number2 ="))
expo=power(num1,num2)
print("power of the input number =",expo)