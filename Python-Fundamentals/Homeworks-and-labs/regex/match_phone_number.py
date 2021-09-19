import re

text = input()
matches = [groups[0] for groups in re.findall(r'(\+359(-| )2\2[0-9]{3}\2[0-9]{4}\b)', text)]
print(", ".join(matches))