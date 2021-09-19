initial_health = 100
initial_bitcoins = 0
alive = True

dungeon_rooms = input().split('|')
best_room = 0

for room in dungeon_rooms:
    best_room += 1
    if "potion" in room:
        command = room.split()
        amount = 100 - initial_health
        if amount < int(command[1]):
            initial_health = 100
            print(f"You healed for {amount} hp.\n"
                  f"Current health: {initial_health} hp.")
        else:
            initial_health += int(command[1])
            print(f"You healed for {command[1]} hp.\n"
                  f"Current health: {initial_health} hp.")
    elif "chest" in room:
        command = room.split()
        initial_bitcoins += int(command[1])
        print(f"You found {command[1]} bitcoins.")
    else:
        command = room.split()
        initial_health -= int(command[1])
        if initial_health <= 0:
            print(f"You died! Killed by {command[0]}.\n"
                  f"Best room: {best_room}")
            alive = False
            break
        else:
            print(f"You slayed {command[0]}.")


if best_room == len(dungeon_rooms) and alive:
    print(f"You've made it!\n"
          f"Bitcoins: {initial_bitcoins}\n"
          f"Health: {initial_health}")