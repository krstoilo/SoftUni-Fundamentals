input_numbers = input()
list_numbers = input_numbers.split(" ")

for i in range(0, len(list_numbers)):
    list_numbers[i] = int(list_numbers[i]) * -1

print(list_numbers)



