import re


def calculate_key(text_input):
    pattern = r"([star]+)"
    if re.search(pattern, text_input, re.I):
        matches = re.findall(pattern, text_input, re.I)
        string_match = ''.join(matches)
        key_count = 0
        for ch in string_match:
            key_count += 1
        return key_count
    return -1


def decrypt_message(text_input, key):
    deciphered = ''
    for ch in text_input:
        deciphered += chr(ord(ch) - key)
    return deciphered


n = int(input())
valid_pattern = r"@([a-zA-Z]+)([^@\-:!>+])*:(\d+)([^@\-:!>+])*!([AD])!([^@\-:!>+])*->(\d+)"

attacked_planets = []
destroyed_planets = []

for message in range(n):
    mess = input()
    mess_key = calculate_key(mess)
    deciphered_mess = decrypt_message(mess, mess_key)
    if re.search(valid_pattern, deciphered_mess):
        matches = re.findall(valid_pattern, deciphered_mess)
        if matches[0][4] == "A":
            attacked_planets.append(matches[0][0])
        else:
            destroyed_planets.append(matches[0][0])


print(f'Attacked planets: {len(attacked_planets)}')
for planet_a in sorted(attacked_planets):
    print(f"-> {planet_a}")
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet_d in sorted(destroyed_planets):
    print(f"-> {planet_d}")