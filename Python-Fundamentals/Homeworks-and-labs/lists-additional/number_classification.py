input_nums = input().split(", ")

positives = [num for num in input_nums if int(num) >= 0]
negatives = [num for num in input_nums if int(num) < 0]
evens = [num for num in input_nums if int(num) % 2 == 0]
odds = [num for num in input_nums if not int(num) % 2 == 0]

print(f'Positive: {", ".join(positives)}')
print(f'Negative: {", ".join(negatives)}')
print(f'Even: {", ".join(evens)}')
print(f'Odd: {", ".join(odds)}')