quantity = int(input())
days_till_C = int(input())

christmas_spirit = 0
total_cost = 0

for day in range(1,days_till_C+1):
    if day % 2 == 0:
        total_cost += quantity * 2
        christmas_spirit += 5
    if day % 3 == 0:
        total_cost += (quantity * 5) + (quantity * 3)
        christmas_spirit += 13
    if day % 5 == 0:
        total_cost += quantity * 15
        christmas_spirit += 17
    if day % 5 == 0 and day % 3 == 0:
        christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += 5 + 3 + 15
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0 and day == days_till_C:
        christmas_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {christmas_spirit}')