phrase = input()
new_phrase = ""

for i in range(0, len(phrase)):
    new_phrase += phrase[i] + phrase[i]

print(new_phrase)