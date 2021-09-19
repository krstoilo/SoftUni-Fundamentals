n = int(input())


for num in range(1,n+1):
    num_str = str(num)
    result = 0
    for char in num_str:
        result += int(char)
    if result == 5 or result == 7 or result == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')