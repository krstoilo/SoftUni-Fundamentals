user_input = input()

for char in user_input:
    if char*2 in user_input:
        user_input = user_input.replace(char*2, char)

print(user_input)