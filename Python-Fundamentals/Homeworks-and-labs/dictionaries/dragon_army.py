n = int(input())

d_type = {}
command = input()

for m in range(n):
    token = command.split()
    type1 = token[0]
    name = token[1]
    damage = token[2]
    if damage == "null":
        damage = 45
    health = token[3]
    if health == "null":
        health = 250
    armor = token[4]
    if armor == "null":
        armor = 10
    if type1 not in d_type:
        d_type[type1] = {}
        d_type[type1][name] = []
        if damage == "null":
            damage = 45
        d_type[type1][name].append(int(damage))
        d_type[type1][name].append(int(health))
        d_type[type1][name].append(int(armor))
    else:
        if name not in d_type[type1]:
            d_type[type1][name] = []
            d_type[type1][name].append(int(damage))
            d_type[type1][name].append(int(health))
            d_type[type1][name].append(int(armor))
        else:
            d_type[type1][name][0] = damage
            d_type[type1][name][1] = health
            d_type[type1][name][2] = armor
    command = input()

print(d_type)
for typ, name in d_type.items():
    print(f"{typ}::()")
    for n, stats in sorted(name.items(), key=lambda x: x[0]):
        print(f"-{n} -> damage:{stats[0]}, health:{stats[1]}, armor:{stats[2]}")