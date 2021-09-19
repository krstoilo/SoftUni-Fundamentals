inventory = input().split()
searched_products = input().split()

stock = {}

for n in range(0, len(inventory), 2):
    key = inventory[n]
    value = int(inventory[n+1])
    stock[key] = value

for product in searched_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")