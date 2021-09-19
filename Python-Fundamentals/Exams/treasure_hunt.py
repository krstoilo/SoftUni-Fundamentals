treasure_chest = input().split("|")
command = input()

while not command == "Yohoho!":
    if 'Loot' in command:
        com = command.split()
        for n in range(1, len(com)):
            if com[n] not in treasure_chest:
                treasure_chest.insert(0, com[n])
    elif 'Drop' in command:
        com = command.split()
        index = int(com[1])
        if 0 <= index < len(treasure_chest):
            item = treasure_chest.pop(index)
            treasure_chest.append(item)
    elif 'Steal' in command:
        com = command.split()
        count = int(com[1])
        if count > len(treasure_chest):
            count = len(treasure_chest)
        stolen = []
        for n in range(count):
            item = treasure_chest.pop()
            stolen.insert(0, item)
        print(", ".join(stolen))
    command = input()


if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    avrg_gain = 0
    for it in treasure_chest:
        avrg_gain += len(it)
    avrg_gain /= len(treasure_chest)
    print(f"Average treasure gain: {avrg_gain:.2f} pirate credits.")