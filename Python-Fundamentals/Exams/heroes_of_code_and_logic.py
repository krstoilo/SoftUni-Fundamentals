hero_count = int(input())
heroes = {}

for n in range(hero_count):
    hero = input().split()
    heroes[hero[0]] = []
    heroes[hero[0]].append(int(hero[1]))
    heroes[hero[0]].append(int(hero[2]))

command = input()
while command != "End":
    if "CastSpell" in command:
        token = command.split(" - ")
        hero_name = token[1]
        mp_needed = int(token[2])
        spell = token[3]
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
    elif "TakeDamage" in command:
        token = command.split(" - ")
        hero_name = token[1]
        damage = int(token[2])
        attacker = token[3]
        if heroes[hero_name][0] - damage > 0:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif "Recharge" in command:
        token = command.split(" - ")
        hero_name = token[1]
        amount = int(token[2])
        if heroes[hero_name][1] + amount > 200:
            curr_mp = heroes[hero_name][1]
            heroes[hero_name][1] = 200
            print(f"{hero_name} recharged for {200 - curr_mp} MP!")
        else:
            heroes[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif "Heal" in command:
        token = command.split(" - ")
        hero_name = token[1]
        amount = int(token[2])
        if heroes[hero_name][0] + amount > 100:
            curr_hp = heroes[hero_name][0]
            heroes[hero_name][0] = 100
            print(f"{hero_name} healed for {100 - curr_hp} HP!")
        else:
            heroes[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")
    command = input()

for member, stats in sorted(heroes.items(), key= lambda x: ((-x[1][0]), x[0])):
    print(member)
    print(f"  HP: {stats[0]}")
    print(f"  MP: {stats[1]}")