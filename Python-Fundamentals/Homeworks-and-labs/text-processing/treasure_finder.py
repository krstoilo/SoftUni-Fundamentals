import re

key = [int(i) for i in input().split()]
text_input = input()
while text_input != 'find':
    new_string = ""
    m = 0
    for n in range(len(text_input)):
        new_string += chr(ord(text_input[n]) - key[m])
        if m == len(key)-1:
            m = 0
        else:
            m += 1
    type_treasure = re.findall(r"&\w+&", new_string)
    coordinates = re.findall(r"<\w+>", new_string)
    print(f"Found {type_treasure[0][1:-1]} at {coordinates[0][1:-1]}")
    text_input = input()