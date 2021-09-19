command_input = input()
price_without_tax = 0
total_tax = 0

while command_input != 'special' and command_input != 'regular':
    command_input = float(command_input)
    if command_input < 0:
        print("Invalid price!")
    else:
        price_without_tax += command_input
        total_tax += 0.2 * command_input
    command_input = input()

total_price_with_tax = price_without_tax + total_tax
final_price = total_price_with_tax

if final_price == 0:
    print("Invalid order!")
else:
    if command_input == "special":
        final_price = total_price_with_tax * 0.9
    else:
        final_price = total_price_with_tax
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_tax:.2f}$\n"
          f"Taxes: {total_tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {final_price:.2f}$")