# question 3 :To check the entered number is armstrong or not ( 371 = 3^3+&^3+1^3 = 371 ) .
def armstrong(a):
    sum=0
    num=a
    b=a
    while b!=0:
        a=b%10
        sum+=a**3
        b=(b//10)
    if sum==num:
        print("armstrong")
    else:
        print("not armstrong")
num=int(input("enter a number ="))
print(armstrong(num))
