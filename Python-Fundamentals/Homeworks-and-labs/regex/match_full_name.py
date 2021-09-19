import re

text = input()
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
to_print = re.findall(pattern, text)

print(' '.join(to_print))