array = [int(i) for i in input().split()]
result = 0

for n in array:
    result = result ^ n

print(result)