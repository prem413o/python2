a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter third number :"))

if(a>b and a>c):
    print("the greatest number is",a)
elif(b>a and b>c):
    print("the greatest number is",b)
else:
    print("the greatest number is ",c)
    