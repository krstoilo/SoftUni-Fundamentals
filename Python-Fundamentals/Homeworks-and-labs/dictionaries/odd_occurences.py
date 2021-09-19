given_sequence = input().split()
dictionary = {}

for word in given_sequence:
    lower_case = word.lower()
    if lower_case not in dictionary:
        dictionary[lower_case] = 0
    dictionary[lower_case] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")

