n = int(input())
list_nums = []
new_list = []

for i in range(n):
    number = int(input())
    list_nums.append(number)

command = input()

if command == 'even':
    for i in list_nums:
        if i % 2 == 0:
            new_list.append(i)
elif command == 'odd':
    for i in list_nums:
        if i % 2 == 1:
            new_list.append(i)
elif command == 'negative':
    for i in list_nums:
        if i < 0:
            new_list.append(i)
elif command == 'positive':
    for i in list_nums:
        if i >= 0:
            new_list.append(i)

print(new_list)