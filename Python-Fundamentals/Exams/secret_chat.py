concealed_message = input()
revealed_message = concealed_message
command = input()
while command != "Reveal":
    token = command.split(":|:")
    if "InsertSpace" in command:
        index = int(token[1])
        revealed_message = revealed_message[:index] + " " + revealed_message[index:]
        print(revealed_message)
    elif "Reverse" in command:
        substring = token[1]
        rev_substring = substring[::-1]
        if substring in revealed_message:
            revealed_message = revealed_message.replace(substring, "", 1)
            revealed_message += rev_substring
            print(revealed_message)
        else:
            print("error")
    elif "ChangeAll" in command:
        substring = token[1]
        replacement = token[2]
        if substring in revealed_message:
            revealed_message = revealed_message.replace(substring, replacement)
        print(revealed_message)
    command = input()

print(f"You have a new text message: {revealed_message}")