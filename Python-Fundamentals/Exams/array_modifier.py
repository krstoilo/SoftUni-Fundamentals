array = [int(i) for i in input().split()]

command = input()
while command != 'end':
    command = command.split()
    if 'swap' in command:
        element_1 = array[int(command[1])]
        array[int(command[1])] = array[int(command[2])]
        array[int(command[2])] = element_1
    elif 'multiply' in command:
        product = array[int(command[1])] * array[int(command[2])]
        array[int(command[1])] = product
    elif 'decrease' in command:
        for n in range(len(array)):
            array[n] -= 1
    command = input()

array = [str(i) for i in array]
print(', '.join(array))
