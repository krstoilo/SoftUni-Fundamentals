target_list = [int(i) for i in input().split()]
command = input()

while command != 'End':
    token = command.split()
    if token[0] == 'Shoot':
        index = int(token[1])
        power = int(token[2])
        if 0 <= index < len(target_list):
            target_list[index] -= power
            if target_list[index] <= 0:
                target_list.pop(index)
    elif token[0] == 'Add':
        index = int(token[1])
        value = int(token[2])
        if 0 <= index < len(target_list):
            target_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif token[0] == 'Strike':
        index = int(token[1])
        radius = int(token[2])
        if 0 <= index-radius and index+radius < len(target_list):
            del target_list[index - radius:index + radius + 1]
        else:
            print("Strike missed!")
    command = input()

target_list = [str(i) for i in target_list]
print('|'.join(target_list))