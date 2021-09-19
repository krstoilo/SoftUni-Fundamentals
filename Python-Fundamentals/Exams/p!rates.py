target_cities = {}

while True:
    target = input()
    if target == "Sail":
        break
    token = target.split("||")
    city_name = token[0]
    people = int(token[1])
    gold = int(token[2])
    if city_name not in target_cities:
        target_cities[city_name] = []
        target_cities[city_name].append(people)
        target_cities[city_name].append(gold)
    else:
        target_cities[city_name][0] += people
        target_cities[city_name][1] += gold

command = input()
while command != "End":
    if "Plunder" in command:
        token = command.split("=>")
        town = token[1]
        people = int(token[2])
        gold = int(token[3])
        target_cities[town][0] -= people
        target_cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if target_cities[town][0] == 0 or target_cities[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            target_cities.pop(town)
    elif "Prosper" in command:
        token = command.split("=>")
        town = token[1]
        gold = int(token[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            target_cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {target_cities[town][1]} gold.")
    command = input()

if len(target_cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(target_cities)} wealthy settlements to go to:")
    for city, data in sorted(target_cities.items(), key=lambda x: (-x[1][1])):
        print(f"{city} -> Population: {data[0]} citizens, Gold: {data[1]} kg")
