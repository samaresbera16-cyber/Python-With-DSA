arr=[1,2,4,5]
n=len(arr)+1
total=n*(n+1)//2
missing=total-sum(arr)
print("missing element is",missing)