bakery_inventory = input().split()
stock = {}

for n in range(0,len(bakery_inventory),2):
    key = bakery_inventory[n]
    value = int(bakery_inventory[n+1])
    stock[key] = value

print(stock)
