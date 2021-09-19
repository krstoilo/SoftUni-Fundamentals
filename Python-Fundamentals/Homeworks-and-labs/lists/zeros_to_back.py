input_list = input().split(', ')

for i in range(len(input_list)):
    if input_list[i] == '0':
        input_list.remove('0')
        input_list.append('0')

input_list = [int(i) for i in input_list]
print(input_list)