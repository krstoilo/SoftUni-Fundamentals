gifts = input().split()
to_remove = 'None'

while True:
    command = input()
    if command == 'No Money':
        break
    command = command.split()
    if command[0] == 'OutOfStock':
        gifts = [sub.replace(command[1], 'None') for sub in gifts]
    elif command[0] == 'Required':
        if int(command[2]) >= len(gifts) or int(command[2]) < 0:
            continue
        gifts[int(command[2])] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

for elem in range(len(gifts)):
    if to_remove in gifts:
        gifts.remove(to_remove)

print(' '.join(gifts))
