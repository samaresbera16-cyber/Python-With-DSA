s="samares"
result=""
for i in range (len(s)):
    if s[i] not in result:
        result=result+s[i]
print("Original String is:", s)
print("After removing duplicates:", result)