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
print("modulus of num1 and num2 =",num1%num2)'''
num=0
while(num<=9):
    num=num+1
    print(num)

