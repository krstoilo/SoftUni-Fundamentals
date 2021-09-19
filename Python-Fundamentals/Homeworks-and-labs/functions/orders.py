product = input()
qty = int(input())


def calculate_price(text, quantity):
    price = None
    if text == "coffee":
        price = 1.50 * quantity
    elif text == "coke":
        price = 1.40 * quantity
    elif text == "water":
        price = 1.00 * quantity
    elif text == "snacks":
        price = 2.00 * quantity
    return price


print(f'{calculate_price(product,qty):.2f}')