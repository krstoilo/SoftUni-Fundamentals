plants_count = int(input())
plants = {}
for i in range(plants_count):
    plant = input().split("<->")
    if plant[0] not in plants:
        plants[plant[0]] = []
        plants[plant[0]].append(int(plant[1]))
    else:
        plants[plant[0]][0] = int(plant[1])

command = input()
while command != "Exhibition":
    if "Rate" in command:
        command = command.replace("Rate: ","")
        token = command.split(" - ")
        plant = token[0]
        rating = int(token[1])
        if plant in plants:
            plants[plant].append(rating)
        else:
            print("error")
    elif "Update" in command:
        command = command.replace("Update: ","")
        token = command.split(" - ")
        plant = token[0]
        new_rarity = int(token[1])
        if plant in plants:
            plants[plant][0] = new_rarity
        else:
            print("error")
    elif "Reset" in command:
        command = command.replace("Reset: ","")
        token = command.split(" - ")
        plant = token[0]
        if plant in plants:
            plants[plant] = plants[plant][:2]
            plants[plant][1] = 0
        else:
            print("error")
    else:
        print("error")
    command = input()

print("Plants for the exhibition:")
for plants, stats in sorted(plants.items(), key=lambda x: (-x[1][0], -sum(j for j in x[1][1:])/len(x[1][1:]))):
    print(f"- {plants}; Rarity: {stats[0]}; Rating: {sum(stats[1:])/len(stats[1:]):.2f}")


