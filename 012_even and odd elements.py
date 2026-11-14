arr=[25,43,18,9,60,67,17,34,5,8,]
odd=0
even=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print("Total even number:", even)
print("Total odd number:", odd)