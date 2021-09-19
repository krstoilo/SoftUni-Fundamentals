lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broke_shield_count = 0

for games in range(1, lost_fights+1):
    if games % 2 == 0:
        expenses += helmet_price
    if games % 3 == 0:
        expenses += sword_price
    if games % 2 == 0 and games % 3 == 0:
        expenses += shield_price
        broke_shield_count += 1
    if broke_shield_count % 2 == 0 and not broke_shield_count == 0:
        expenses += armor_price
        broke_shield_count = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")