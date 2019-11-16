Username=input("Enter your Username =")
Password =input("Enter your Password2 =")
if Username=="SANJAY" and Password =="PANDIT":
    print("WELCOME",Username,Password,"NOW YOU CAN GO FOR FURTHER PROCESSING!")
else:
    print("Plesae check yor UserName and Password")
number1=int(input("Enterd first number ="))
number2=int(input("Enterd second number ="))
sum=number1+number2
value=int(input("enter the sum of number1 and number2 ="))
if sum==value:
        print("you can use calculator")
else:
        print("you cannot use calculator")
def Add(num1,num2):
    return num1+num2
def Subtract(num1,num2):
    return num1-num2
def Multiply(num1,num2):
    return num1*num2
def Divide(num1,num2):
    return num1/num2
def Quotient(num1,num2):
    return num1//num2
def Reminder(num1,num2):
    return num1%num2
def power(num1,num2):
    return num1**num2
import math
def sqrt(num1):
    return math.sqrt(num1)
print("Select the operation you want to perform")
print("1.Add    2.Subtract     3.Multiply      4.Divide     5.Reminder     6.Quotient      7.Power      8.Square Root")
Choice=int(input("Enter your choice(1/2/3/4/5/6/7/8):"))
if Choice == 1:
    num1 = int(input("Enter first number ="))
    num2 = int(input("Enter second number ="))
    print("Sum of num1 and num2 =",num1+num2)
elif Choice == 2:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    print("Difference of num1 and num2 =", num1 - num2)
elif Choice == 3:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    print("Multiplication of num1 and num2 =", num1 * num2)
elif Choice == 4:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    print("Division of num1 and num2 =", num1 / num2)
elif Choice == 5:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    print("Quotient after dividing num1 and num2 =", num1 // num2)
elif Choice == 6:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    print("Reminder after dividing num1 and num2 =", num1 % num2)
elif Choice == 7:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    print("Power of num1 by num2 =", num1 ** num2)
elif Choice == 8:
    num=int(input("Enter first number ="))
    print("Square Root of first number =", sqrt(num))
else:
    print("Choice of opreation out of range")