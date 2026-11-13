n=int(input("Enter a  number:"))
if(n>1):
    for i in (2,n):
        if (n%i)==0:
            print("Not Prime.")
            break
        else:
            print("Prime number.")
            break
else:
    print("Prime number.")