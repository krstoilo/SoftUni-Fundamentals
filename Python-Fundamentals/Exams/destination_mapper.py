import re

map_places = input()
pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"
matches = re.findall(pattern, map_places)
destinations = []
travel_points = 0
for n in range(len(matches)):
    destinations.append(matches[n][1])
for place in destinations:
    travel_points += len(place)

dest_string = ', '.join(destinations)

print(f"Destinations: {dest_string}")
print(f"Travel Points: {travel_points}")
