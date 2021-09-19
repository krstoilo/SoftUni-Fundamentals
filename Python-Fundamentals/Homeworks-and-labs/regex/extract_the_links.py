import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = " ".join(lines)

pattern = r"(www.[a-zA-Z0-9-]+(\.[a-z]+)(\.[a-z]+)*)"
matches = re.findall(pattern, text)

for match in matches:
    print(match[0])