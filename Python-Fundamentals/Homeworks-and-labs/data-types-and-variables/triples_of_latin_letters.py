n = int(input())

for n1 in range(97, 97 + n):
    for n2 in range(97, 97+n):
        for n3 in range(97, 97 + n):
            print(f'{chr(n1)}{chr(n2)}{chr(n3)}')