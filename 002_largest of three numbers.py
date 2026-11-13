a = int(input("Enter the value of A:"))
b = int(input("Enter the value of B:"))
c = int(input("Enter the value of C:"))
if(a>b and a>c):
    print("The largest number is:",a)
elif(b>c and b>a):
    print("The largest number is:",b)
else:
    print("The largest number is:",c)