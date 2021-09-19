given_materials = input().lower().split()
value = False

junk = {}
key_materials = {
    "fragments": 0,
    "motes": 0,
    "shards": 0
}

while value is False:
    for n in range(1, len(given_materials), 2):
        item = given_materials[n]
        quantity = int(given_materials[n-1])
        if item in key_materials:
            key_materials[item] += quantity
            if item == 'fragments':
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print(f"Valanyr obtained!")
                    value = True
                    break
            elif item == 'motes':
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print(f"Dragonwrath obtained!")
                    value = True
                    break
            elif item == 'shards':
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print(f"Shadowmourne obtained!")
                    value = True
                    break
        else:
            if item in junk:
                junk[item] += quantity
            else:
                junk[item] = quantity
    if value is True:
        break
    given_materials = input().lower().split()

sorted_key_materials = sorted(key_materials.items(), key=lambda x: x[1], reverse=True)
for (key, value) in sorted_key_materials:
    print(f"{key}: {value}")

sorted_junk = sorted(junk.items(), key=lambda x: x[0])
for (key, value) in sorted_junk:
    print(f"{key}: {value}")