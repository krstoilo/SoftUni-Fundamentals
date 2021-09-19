import re

text = input()
pattern = r"(?<=\s)([a-z0-9]+[\._-]?\w+@[a-z0-9-]+\.[a-z0-9-]+\.?\w*)\b"

matches = re.findall(pattern, text)

for match in matches:
    print(match)
