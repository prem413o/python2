marks=int(input("Enter your marks: "))

if(marks>=90):
    print("pass with A+")
elif(marks>80 and marks<90):
    print("pass with A")
elif(marks>60 and marks<=80):
    print("pass with B+")
else:
    print("Fail with E")