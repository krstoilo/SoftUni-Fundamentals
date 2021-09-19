import re

text = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
nums = re.finditer(pattern, text)

for n in nums:
    print(n.group(0), end=" ")