import sys

numbers = [int(i) for i in input().split()]
num = int(input())


def find_smallest(numbers_list):
    smallest = sys.maxsize
    for n in numbers_list:
        if n < smallest:
            smallest = n
    return smallest


for turns in range(num):
    numbers.remove(find_smallest(numbers))

numbers = [str(i) for i in numbers]
print(", ".join(numbers))