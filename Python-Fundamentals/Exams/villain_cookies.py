biscuit_list = input().split(", ")
command = input()

while not command == "No More Money":
    if "OutOfStock" in command:
        tokens = command.split()
        biscuit = tokens[1]
        biscuit_list = [None if v == biscuit else v for v in biscuit_list]
    elif "Required" in command:
        tokens = command.split()
        biscuit = tokens[1]
        index = int(tokens[2])
        if 0 <= index < len(biscuit_list):
            if not biscuit_list[index] is None:
                biscuit_list[index] = biscuit
    elif "Last" in command:
        tokens = command.split()
        biscuit = tokens[1]
        biscuit_list.append(biscuit)
    command = input()

biscuit_list = [el for el in biscuit_list if el is not None]
print(" ".join(biscuit_list))



