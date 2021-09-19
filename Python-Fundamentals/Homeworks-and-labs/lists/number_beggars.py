number_list = input()
beggars = int(input())

number_list = number_list.split(", ")
beggar_income = []

for i in range(beggars):
    beggar_income.append(0)

if beggars >= len(number_list):
    for i in range(0, len(number_list)):
        beggar_income[i] = int(number_list[i])
else:
    for beggar_count in range(beggars):
        for turns in range(beggar_count, len(number_list), beggars):
            beggar_income[beggar_count] += int(number_list[turns])

print(beggar_income)