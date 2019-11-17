'''
# examlple 1 armstrong number
num=143
w=int(num/10) #int(num/10)= 15 so [ w=15 ]
x=num%10 # num=153 so modlus operator is used to get the reminder value from 153 i.e 3 [ x=3 ]
y=int(w/10) #int(w/10)=1 so [ y=1 ]
z=w%10 # w =15 so modlus operator is used to get the reminder value from 15 i.e 5 [ x=5 ]
sum=(x**3+y**3+z**3)
print("num=",num)
print ("w=",w)
print("x=",x)
print("y=",y)
print("z=",z)
if num==sum:
    print(num," is armstrong number")
else:
    print(num," is not armstrong number")
#example 2 multiplication program
num =3
for i in range (1,10):
        print(num,"*",i,"=",num*i)
# example 3 print hello stepwise
#print("h\ne\nl\nl\no\n")
#print("h\be\bl\bl\bo\b")
#print("h\te\tl\tl\to\t")
#print("h\ae\al\al\ao\a")
# example 4 using input satatement name,age and arithmetic calculation
name="sanjay kumar pandit"
age=22
print("My name is ",name ," and my age is ",age )
name= input("enter name")
age=input("enter gae")
num1=int(input("enter num1"))
num2=int(input("enter num2"))
#print("My name is ",name ," and my age is ",age )
print("sum =",num1+num2)
print("subtraction=",num1-num2)
print("multiply=",num1*num2)
print("division=",num1/num2)
print("exponential of num1 =",num1**3," and exponential of num1 =",num2**3)
print("modulus of num1 and num2 =",num1%num2)
# example 5 series of number
num=0
while(num<=9):
    num=num+1
    print(num)
    break
# example 6 program for list
list1=[1,2,8,5,4,7]
list2=[3,6,9,10]
#print(list1)
print(list2)
list1.append("kanchan")
list1.pop(6)
list1.sort()
list1.sort(reverse=True)
print(list1.count(7))
list1.extend(list2)
print(list1)
print(list1.sort())
list3=["sanjay","ajay","kanchan"]
list3.append("manoj") # in list append  work for strings
print(list3)
# example 7 program for tuples
tuple1=("sanjay","ajay","kanchan",'s')
tuple2=("pravin","nabin","dikshya")
tuple3=(1,5,4,7,3,8)
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple1.count("sanjay")) # count() works for string and integer in tuple
print("sanjay" in (tuple1))
#print(tuple1.extend(tuple2))
#tuple1.sort() # sort() don't work for string in tuple
#tuple3.sort() # sort() don't work for integer in tuple
tuple3.append() # append() don't work for string and integer in tuple ( tuple has no attribute for sort(),
append(),pop(),extend()
# example 8 = five subject mark from user and input into list and ptint sum of all marks
mark=[]
math=int(input("enter the mark of math ="))
science=int(input("enter the mark of science ="))
nepali=int(input("enter the mark of nepali ="))
computer=int(input("enter the mark of computer ="))
social=int(input("enter the mark of social ="))
mark.append(math)
mark.append(science)
mark.append(nepali)
mark.append(computer)
mark.append(social)
print(mark)
OM=math+science+nepali+computer+social
print("obtained mark of five subject = ",OM)
# Example 9 take input from the user and ask the user which string needs to be counted
user=input("enter a string = ")
user1=input("which stringneed u ant to count = ")
print(user1.count(user1))
# Example 10 replace a word from the stringand convert the string in uppercase
list1=[1,4,2,6,7]
print(max(list1))
print(min(list1))
Name="SANJAY KUMAR PANDIT"
print(Name)
print (Name.replace("SANJAY","AJAY"))
print(Name.swapcase())
# EXAMPLE 11 if statement going fro party.
num=int(input ("enter the amount of money you have ="))
if num>0:
    print("you can go to party")
    print("congratulation you can go to party")
else:
    print("you can't go to party")
    print("sorry you can't go to party")
# EXAMPLE 12 if statement pass or fail.
num=int(input ("enter the passing number="))
if num>=40:
    print("you are pass")
else:
    print("you are fail")
# EXAMPLE 13 if statement driving according to age.
age=int(input ("enter your age ="))
if age>=18:
    print("you can drive")
else:
    print("you can't drive")
# example 14 using elif grage A,B,C and fail
mark=int(input("enter your obtained mark ="))
if mark>=90 and mark<100:
    print("you  got A")
elif mark>=70 and mark<90:
    print("you got B")
elif mark>=40 and mark<70:
    print("you got c")
elif mark<40 and mark>=0:
    print("you are fail")
else:
    print("entered mark not valid")
# example 15 even or odd
num=int(input("enter a number ="))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

if num>0:
   print ("ok")
else:
    print("out of range")
# example 16 leap year or not
year=int(input("enter a number ="))
if year%4==0:
    print(year,"year is leap")
else:
    print(year,"year is not leap")
# example 17 ask from user naem,age and mobile number and should be valid [ isdigit(),isalpha() and isnull() ]
# validation name
name=input("enter your name =")
if name.isalpha()==True and len(name)>7 or ' ' in name:
    print(name, "valid")
else:
    print(name, "is invalid")
age=input("enter your age =")
# validation age
if age.isnumeric()==True and int(age)>=18 or ' ' in age:

    print(age,"valid")
else:
    print(age, "is invalid")
# validation mobile
mobile=input("enter your mobile number =")
if mobile.isnumeric()==True and len(mobile)==10 or ' ' in mobile:
    print(mobile,"valid")
else:
    print(mobile, "is invalid")
# example 18 to identify which polygon figure is the entered value shows
AB=int(input("enter the length ="))
BC=int(input("enter the breadth ="))
CD=int(input("enter the length ="))
AD=int(input("enter the breadth ="))
if AB==CD and BC==AD:#AB==BC==CD==AD:
    print("it is a rectangle")
elif AB==BC==CD==AD:#AB==CD and BC==AD:
    print("It is a square")
else:
    print("entered value is no match the condition ")
#example 19 leap year
year=int(input("enter the value of year ="))
if year%4==0:
    print(year,"is leap")
elif year%100==0:
    print(year,"yearis leap")
elif year%400==0:
    print(year,"is leap")
else:
    print(year,"is not leap")
'''# example 20 to check enterded value match or not ,not match then again check if match then welcome
name1=input("enter your name =")
while name1.isalpha()==False or len(name1)<7:
    if  ' ' in name1:
        break
    print("entered name don't match")
    name1=input("enter your name")
print("welcome now you can go to next step")
#age=input("enter your age =")
''''while age.isdigit()==False or int(age)<18:
    print("entered name don't match")
    age = input("enter your age")
    print("welcome now you can go to next step")
mobile=input("enter the mobile number =")
while len(mobile)!=10:
    print("entered name don't match")
    mobile = input("enter your mobile number =")
else:
    print("welcome now you can go to next step")
#example 21 ( Ask the user to enter 10 numbers using only one input statement and add them to the List. )
number=input("Enter multiple value: ").split()
x=number
print("Number of list is: ",x)
# example 22 ( From a list of numbers make a new list containing only the even numbers.)
list1=[1,2,3,4,5,6,7,8,9,10]
print("the value of list1 =",list1)
num=[]
for num1 in list1:
    num2=num1
    if num2 % 2==0:
         num.append(num2)
print("even number in the list are",num)
print(type(num))
##example 22 multiplication program
num =3
for i in range (1,10):
        print(num,"*",i,"=",num*i)
# eexample 23 From a list separate the integers , strings and floats elements into three different lists.
import sys
list=[1,2,3,0,4,9.8,3.7,6.8,"nishan","sanjay","suwas","bhagat"]
list1=[]
list2=[]
list3=[]
for x in list:
    if type(x)==int:
        list1.append(x)
    elif type(x) ==float:
        list2.append(x)
    elif type(x)==str:
        list3.append(x)
else:
        sys.exit
print("list1=",list1)
print("list2=",list2)
print("list3=",list3)
# example 24 From a list ask the user the number he wants to remove from the list and then print the list.
list1=[1,2,3,4.6,5.9,6.7,"nishan","sanjay"]
index=int(input("enter the index ="))
del list1[index]
print("list1=",list1)'''
