text = input()
letters = []
digits = []
chars = []

for ch in text:
    if ch.isalpha():
        letters.append(ch)
    elif ch.isdigit():
        digits.append(ch)
    else:
        chars.append(ch)

print(''.join(digits))
print(''.join(letters))
print(''.join(chars))