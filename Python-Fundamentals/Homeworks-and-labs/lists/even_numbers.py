input_string = input().split(', ')
numbers = [int(i) for i in input_string]

even_indices = []

for n in range(len(numbers)):
    if numbers[n] % 2 == 0:
        even_indices.append(n)

print(even_indices)
