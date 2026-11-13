arr = [10,25,5,45,30]
small = arr[0]
for i in range(len(arr)):
    if arr[i] < small:
        small = arr[i]
print("Smallest element:", small)