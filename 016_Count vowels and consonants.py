s= "Hello World! This is Samares Bera!"
vowels=0
consonants=0
for i in range (len(s)):
     if s[i].lower() in "aeiou":
         vowels+=1
     elif s[i].isalpha():
          consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

