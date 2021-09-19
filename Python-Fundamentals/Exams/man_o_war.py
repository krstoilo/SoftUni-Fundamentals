pirate_ship = [int(i) for i in input().split('>')]
warship = [int(i) for i in input().split('>')]
max_health = int(input())
stalemate = True


def index_valid(index, list_length):
    if 0 <= index < list_length:
        return True
    else:
        return False


def ship_status(ship_sections):
    status_count = 0
    for section in ship_sections:
        status_count += section
    return status_count


def defend(start_index, end_index, damage, attacked_ship):
    for n in range(start_index, end_index+1):
        attacked_ship[n] -= damage
    return attacked_ship


command = input()
while command != 'Retire':
    command = command.split()
    if 'Fire' in command:
        if index_valid(int(command[1]), len(warship)):
            warship[int(command[1])] -= int(command[2])
            if warship[int(command[1])] - int(command[2]) <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    if not stalemate:
        break
    elif 'Defend' in command:
        if index_valid(int(command[1]), len(pirate_ship)):
            if index_valid(int(command[2]), len(pirate_ship)):
                pirate_ship = defend(int(command[1]), int(command[2]), int(command[3]), pirate_ship)
                for p in range(len(pirate_ship)):
                    if pirate_ship[p] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        stalemate = False
                        break
    if not stalemate:
        break
    elif 'Repair' in command:
        if index_valid(int(command[1]), len(pirate_ship)):
            if int(command[2]) + pirate_ship[int(command[1])] <= max_health:
                pirate_ship[int(command[1])] += int(command[2])
            else:
                pirate_ship[int(command[1])] = max_health
    elif 'Status' in command:
        count = 0
        for sections in pirate_ship:
            if sections < 0.2 * max_health:
                count += 1
        print(f"{count} sections need repair.")
    command = input()


if stalemate:
    print(f"Pirate ship status: {ship_status(pirate_ship)}")
    print(f"Warship status: {ship_status(warship)}")