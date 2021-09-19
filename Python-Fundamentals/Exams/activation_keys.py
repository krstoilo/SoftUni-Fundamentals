raw_key = input()
command = input()
a_key = ""

while command != "Generate":
    if "Contains" in command:
        token = command.split(">>>")
        if token[1] in raw_key:
            print(f'{raw_key} contains {token[1]}')
        else:
            print("Substring not found!")
    elif "Flip" in command:
        token = command.split(">>>")
        if token[1] == "Lower":
            temp = raw_key[int(token[2]):int(token[3])]
            lowered_temp = temp.lower()
            raw_key = raw_key[:int(token[2])] + lowered_temp + raw_key[int(token[3]):]
            print(raw_key)
        elif token[1] == "Upper":
            temp = raw_key[int(token[2]):int(token[3])]
            uppered_temp = temp.upper()
            raw_key = raw_key[:int(token[2])] + uppered_temp + raw_key[int(token[3]):]
            print(raw_key)
    elif "Slice" in command:
        token = command.split(">>>")
        raw_key = raw_key[:int(token[1])] + raw_key[int(token[2]):]
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")