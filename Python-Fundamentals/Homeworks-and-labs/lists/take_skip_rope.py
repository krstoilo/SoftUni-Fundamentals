encrypted_message = input()

numbers_list = []
symbols_list = []

for n in range(len(encrypted_message)):
    if encrypted_message[n].isdigit():
        numbers_list.append(int(encrypted_message[n]))
    else:
        symbols_list.append(encrypted_message[n])

take_list = []
skip_list = []

for i in range(len(numbers_list)):
    if i % 2 == 0 or i == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

count = 0
skips = 0
result = []

for n in range(len(take_list)):
    result.extend(symbols_list[skips:skips+take_list[n]])
    count = take_list[n]
    skips += skip_list[n] + count

print(''.join(result))