import re

input_text = input()
regex_pattern = r'([*]{2}|[:]{2})([A-Z]{1}[a-z]{2,})(\1)'
cool_threshold = 1
emojis = re.findall(regex_pattern, input_text)
cool_emojis = []

for char in input_text:
    if char.isdigit():
        cool_threshold *= int(char)

for emoji in emojis:
    coolness = 0
    for ch in emoji[1]:
        coolness += ord(ch)
    if coolness >= cool_threshold:
        cool_emojis.append(emoji)


print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for n in cool_emojis:
    print("".join(n))