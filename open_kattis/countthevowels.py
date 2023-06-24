sentence = input("")
sentence = sentence.upper()
lst = []
count = 0

for i in sentence:
    lst.append(i)

vowels = ("A", "E","I", "O","U")

for i in range(len(lst)):
    if lst[i] in vowels:
        count += 1

print(count)