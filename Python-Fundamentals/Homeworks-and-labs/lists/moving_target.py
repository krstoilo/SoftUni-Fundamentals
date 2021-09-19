def shoot_com(index, power, seqnce):
    if len(seqnce) > index:
        seqnce[index] -= power
        if seqnce[index] <= 0:
            del seqnce[index]
    return seqnce


def add_com(index, value, seqnce):
    if len(seqnce) > index:
        seqnce.insert(index, value)
    else:
        print('Invalid placement!')
    return seqnce


def strike_com(index, radius, seqnce):
    if len(seqnce) >= (index + 2 * radius):
        del seqnce[(index - radius):(index + radius + 1)]
    else:
        print('Strike missed!')
    return seqnce


targets_sequence = [int(i) for i in input().split()]

command = input().split()

while not command[0] == 'End':
    if 'Shoot' in command:
        shoot_com(int(command[1]), int(command[2]), targets_sequence)
    elif 'Add' in command:
        add_com(int(command[1]), int(command[2]), targets_sequence)
    elif 'Strike' in command:
        strike_com(int(command[1]), int(command[2]), targets_sequence)
    command = input().split()

targets_sequence = [str(i) for i in targets_sequence]
print('|'.join(targets_sequence))