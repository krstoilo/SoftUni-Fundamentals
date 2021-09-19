check = {}

command = input()
while command != 'buy':
    command = command.split()
    product = command[0]
    price = float(command[1])
    qty = int(command[2])
    total = 0
    if product not in check:
        check[product] = [price, qty, total]
    else:
        if check[product][0] != price:
            check[product][0] = price
        check[product][1] += qty
    command = input()

for (item, info) in check.items():
    info[2] = info[0] * info[1]

for (key, value) in check.items():
    print(f"{key} -> {value[2]:.2f}")