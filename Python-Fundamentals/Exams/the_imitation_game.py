encryp_msg = input()

command = input()
while command != "Decode":
    token = command.split("|")
    if token[0] == "Move":
        letter_count = int(token[1])
        moved_letters = encryp_msg[:letter_count]
        encryp_msg = encryp_msg[letter_count:]
        encryp_msg = encryp_msg + moved_letters
    elif token[0] == "Insert":
        index = int(token[1])
        value = token[2]
        if 0 <= index <= len(encryp_msg):
            encryp_msg_first = encryp_msg[:index]
            encryp_msg_second = encryp_msg[index:]
            encryp_msg = encryp_msg_first + value + encryp_msg_second
    elif token[0] == "ChangeAll":
        substring = token[1]
        replacement = token[2]
        if substring in encryp_msg:
            encryp_msg = encryp_msg.replace(substring, replacement)
    command = input()

print(f'The decrypted message is: {encryp_msg}')