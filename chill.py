'''
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
#multiplication program
num =3
for i in range (1,10):
        print(num,"*",i,"=",num*i)
#print("h\ne\nl\nl\no\n")
#print("h\be\bl\bl\bo\b")
#print("h\te\tl\tl\to\t")
#print("h\ae\al\al\ao\a")
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
num=0
while(num<=9):
    num=num+1
    print(num)
    break
# program for list
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
# program for tuples
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
# example 1 = five subject mark from user and input into list and ptint sum of all marks
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
print("obtained mark of five subject = ",OM)'''
# Example take input from the user and ask the user which string needs to be counted
user=input("enter a string = ")
user1=input("which stringneed u ant to count = ")
print(user1.count(user1))
