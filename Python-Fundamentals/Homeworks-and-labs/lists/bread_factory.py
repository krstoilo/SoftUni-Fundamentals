day_events = input().split('|')
energy = 100
coins = 100
is_not_bankrupt = True

for event in day_events:
    type_event, number = event.split('-')


    if 'rest' in event:
        gained_energy = 0

        if energy + int(number) > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += int(number)
            gained_energy = int(number)

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif 'order' in event:
        if energy > 30:
            energy -= 30
            coins += int(number)
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print('You had to rest!')


    else:
        if coins >= int(number):
            coins -= int(number)
            print(f'You bought {type_event}.')
            continue
        if coins < int(number):
            print(f'Closed! Cannot afford {type_event}.')
            is_not_bankrupt = False
            break

        if coins <= 0:
            is_not_bankrupt = False
            break

if is_not_bankrupt:
    print(f'Day completed!')
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")