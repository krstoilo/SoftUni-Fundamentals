list_1 = input().split(', ')
list_2 = input().split(', ')

result = []

for i in range(len(list_1)):
    word = list_1[i]
    for n in range(len(list_2)):
        if word in list_2[n] and not word in result:
            result.append(word)

print(result)
