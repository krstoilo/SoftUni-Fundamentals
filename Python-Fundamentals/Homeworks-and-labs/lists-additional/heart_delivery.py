neighborhood_places = [int(i) for i in input().split("@")]
command = input()
cupid_pos = 0
failed_houses = 0

while command != "Love!":
    command = command.split()
    jump = int(command[1])
    cupid_pos += jump
    if cupid_pos < len(neighborhood_places):
        pass
    else:
        cupid_pos = 0
    if neighborhood_places[cupid_pos] <= 0:
        print(f"Place {cupid_pos} already had Valentine's day.")
    else:
        neighborhood_places[cupid_pos] -= 2
        if neighborhood_places[cupid_pos] == 0:
            print(f"Place {cupid_pos} has Valentine's day." )
    command = input()

for house in neighborhood_places:
    if not house == 0:
        failed_houses += 1

print(f"Cupid's last position was {cupid_pos}.")
if failed_houses > 0:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")