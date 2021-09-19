n = int(input())
word = input()

list_strings = []
filtered_string = []

for i in range(n):
    string = input()
    list_strings.append(string)

print(list_strings)

for i in range(len(list_strings) - 1, -1, -1):
    element = list_strings[i]
    if word not in element:
        list_strings.remove(element)

print(list_strings)
