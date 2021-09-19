secret_message = input().split()
deciphered_message = []

for word in secret_message:
    deciphered_wrd = ""
    list_msg = []
    code = ''
    for ch in word:
        if ch.isdigit():
            code += ch
        else:
            list_msg.append(ch)
    if len(list_msg) > 1:
        deciphered_wrd += chr(int(code)) + list_msg[-1] + ''.join(list_msg[1:-1]) + list_msg[0]
    else:
        deciphered_wrd += chr(int(code)) + list_msg[0]
    deciphered_message.append(deciphered_wrd)

print(" ".join(deciphered_message))


