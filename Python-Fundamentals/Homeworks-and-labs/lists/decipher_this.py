def decipher_word(word):
    code = ""
    for char in word:
        if char.isdigit():
            code += char
    code = int(code)
    new = [char for char in word if not char.isdigit()]
    new.insert(0, chr(code))
    character = new[1]
    new[1] = new[-1]
    new[-1] = character
    return "".join(new)


message = input().split()
result = ""

for word in message:
    print(decipher_word(word), end=" ")


