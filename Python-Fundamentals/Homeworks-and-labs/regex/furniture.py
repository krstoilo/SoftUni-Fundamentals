import re

furniture_input = input()
#">>{furniture name}<<{price}!{quantity}"
pattern = r">>((\w+ *)+)<<(\d+.?\d*)\!(\d+)"
valid_furniture = []
total_price = 0
n = 0

while furniture_input != 'Purchase':
    if re.search(pattern, furniture_input):
        valid_furniture.append(re.findall(pattern, furniture_input))
        qty = valid_furniture[n][0][3]
        price = valid_furniture[n][0][2]
        total_price += int(qty) * float(price)
        n += 1
    furniture_input = input()

print("Bought furniture:")
for el in valid_furniture:
    print(el[0][0])
print(f'Total money spend: {total_price:.2f}')