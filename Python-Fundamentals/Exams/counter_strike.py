energy = int(input())

won_battles = 0
game_lost = False

command = input()
while command != 'End of battle':
    if command.isdigit():
        command = int(command)
    if energy < command:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        game_lost = True
        break
    else:
        energy -= command
        won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles
    command = input()

if not game_lost:
    print(f"Won battles: {won_battles}. Energy left: {energy}")