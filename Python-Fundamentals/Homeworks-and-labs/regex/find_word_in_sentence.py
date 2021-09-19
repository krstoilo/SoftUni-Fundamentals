import re

text = input()
word = input()
pattern = f"{word}\W"
matches = re.findall(pattern, text, re.I)
print(len(matches))