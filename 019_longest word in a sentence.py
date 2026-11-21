s="Python programming is very interesting"
words=s.split()
longest=""
for i in range(len(words)):
    if len(words[i])>len(longest):
        longest=words[i]
print("Longest word:", longest)
print("Length:", len(longest))