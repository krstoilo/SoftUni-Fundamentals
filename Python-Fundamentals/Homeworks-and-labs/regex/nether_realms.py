import re


def calculate_health(demon_name):
    health_points = 0
    pattern = r'([^0-9*/\-\.\+])'
    counted_chars = re.findall(pattern, demon_name)
    for char in counted_chars:
        health_points += ord(char)
    return health_points


def calculate_damage(demon_name):
    damage_points = 0
    pattern = r'((-?\d+)(\.\d+)?)'
    numbers = re.findall(pattern, demon_name)
    new_numbers = []
    for n in range(len(numbers)):
        new_numbers.append(numbers[n][0])
    for num in new_numbers:
        if "-" in num:
            temp = float(num.replace("-", ""))
            damage_points -= temp
        else:
            damage_points += float(num)
    for ch in demon_name:
        if ch == "*":
            damage_points *= 2
        elif ch == "/":
            damage_points /= 2
    return damage_points


# find names by splitting multiple spaces in the input string
names_input = input()
cleared_names = re.split(r'\s*,\s*|,\s*', names_input)
demon_book = {}
for name in cleared_names:
    demon_book[name] = []
    demon_book[name].append(calculate_health(name))
    demon_book[name].append(calculate_damage(name))

for demon, stats in sorted(demon_book.items(), key=lambda x: x[0]):
    print(f"{demon} - {stats[0]} health, {stats[1]:.2f} damage")
