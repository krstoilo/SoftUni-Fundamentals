cities = {'Tortuga': [270000, 870], 'Santo Domingo': [240000, 810], 'Havana': [410000, 1100]}

print(cities.items())
keys = list(cities.keys())
print(keys)
gold = cities["Tortuga"][1]
print(gold)
sorted_c = sorted(cities.items(), key=lambda x: (-x[1][1]))
print(sorted_c)