import sys

numbers = input().split()
n_remove = int(input())
numbers = [int(i) for i in numbers]

min_numbers = sys.maxsize

for removals in range(n_remove):
    for iteration in range(len(numbers)):
        if numbers[iteration] < min_numbers:
            min_numbers = numbers[iteration]
    numbers.remove(min_numbers)
    min_numbers = sys.maxsize

print(numbers)