import re

total_income = 0
pattern = r"((%[A-Z]{1}[a-z]+%)([^\|\$%\.]+)*(<[\w]+>)([^\|\$%\.]+)*" \
          r"(\|\d+\|)([^\|\$%\.\d]+)*(\d+\.*\d*\$))"

customers = []
products = []
qty = []
prices = []

order = input()
while order != "end of shift":
    if re.search(pattern, order):
        matches = re.findall(pattern, order)
        customers.append(matches[0][1][1:-1])
        products.append(matches[0][3][1:-1])
        qty.append(int(matches[0][5][1:-1]))
        prices.append(float(matches[0][7][:-1]))
    order = input()

for n in range(len(customers)):
    print(f"{customers[n]}: {products[n]} - {qty[n] * prices[n]:.2f}")
    total_income += qty[n] * prices[n]
print(f"Total income: {total_income:.2f}")
