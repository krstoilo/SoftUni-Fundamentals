text_input = input().split()
occurrences = {}

for text in text_input:
    for char in text:
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1

for (char, count) in occurrences.items():
    print(f"{char} -> {count}")




