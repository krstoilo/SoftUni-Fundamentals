user_input = input()
ciphered = []

for char in user_input:
    ciphered.append(chr(ord(char)+3))

print("".join(ciphered))