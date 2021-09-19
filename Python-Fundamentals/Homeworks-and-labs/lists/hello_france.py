items = input().split('|')
budget = float(input())
isWorth = False
prices = []
overprices = []
profit = 0

for item in items:
    type_item, price = item.split('->')

    if 'Clothes' in item and float(price) <= 50:
        isWorth = True
    elif 'Shoes' in item and float(price) <= 35:
        isWorth = True
    elif 'Accessories' in item and float(price) <= 20.5:
        isWorth = True

    if isWorth:
        if budget >= float(price):
            budget -= float(price)
            prices.append(float(price))

    isWorth = False

for it in prices:
    overprice = it + 0.4*it
    overprices.append(overprice)
    profit += (overprice - it)

for it in overprices:
    budget += it

for n in range(len(overprices)):
    print(f'{overprices[n]:.2f}', end=" ")
print()

print(f'Profit: {profit:.2f}')
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")