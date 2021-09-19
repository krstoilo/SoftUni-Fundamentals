neighborhood = [int(i) for i in input().split('@')]

command = input().split()

last_position = 0
houses_count = len(neighborhood)

while not command[0] == 'Love!':
    for n in range(int(command[1])):
        last_position += 1
        if last_position >= len(neighborhood):
            last_position = 0
    if neighborhood[last_position] <= 0:
        print(f"Place {last_position} already had Valentine's day.")
    if neighborhood[last_position] - 2 == 0:
        print(f"Place {last_position} has Valentine's day.")
        houses_count -= 1
    neighborhood[last_position] -= 2
    command = input().split()

print(f"Cupid's last position was {last_position}.")
if houses_count == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {houses_count} places.")