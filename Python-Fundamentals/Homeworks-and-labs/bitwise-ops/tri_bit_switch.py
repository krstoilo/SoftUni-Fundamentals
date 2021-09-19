num = int(input())
position = int(input())

mask = 7 << position
result = num ^ mask
print(result)