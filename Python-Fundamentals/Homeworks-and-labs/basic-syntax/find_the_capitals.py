string = input()
list = []

for elem in range(0, len(string)):
    if string[elem].isupper():
        list.append(elem)

print(list)
