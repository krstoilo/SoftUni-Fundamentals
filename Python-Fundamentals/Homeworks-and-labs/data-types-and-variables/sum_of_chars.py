count_n = int(input())
sum = 0

for ch in range(count_n):
    letter = input()
    sum += ord(letter)

print(f'The sum equals: {sum}')