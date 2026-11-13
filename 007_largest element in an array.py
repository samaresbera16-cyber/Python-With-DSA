arr = [10,25,5,45,30]
largest = arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print("Largest element:", largest)