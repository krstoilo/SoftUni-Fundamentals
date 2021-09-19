import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = " ".join(lines)

pattern = r"\d+"
nums = re.findall(pattern, text)
print(" ".join(nums))