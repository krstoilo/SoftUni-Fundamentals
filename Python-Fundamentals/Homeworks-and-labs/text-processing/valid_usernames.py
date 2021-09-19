text_input = input().split(", ")
valid_users = []

for name in text_input:
    if 3 <= len(name) <= 16:
        contains_symbol = False
        for char in name:
            if not char.isalpha() and not char.isdigit() and char != "-" and char != "_":
                contains_symbol = True
                break
        if contains_symbol:
            pass
        else:
            valid_users.append(name)

for n in valid_users:
    print(n)