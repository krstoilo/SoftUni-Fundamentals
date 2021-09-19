given_list = input().split()
k = int(input())

result = []

given_list = [int(i) for i in given_list]

while len(given_list) is not 0:
    for i in range(1, len(given_list), k-1):
        result.append(given_list[i])
        del given_list[i]

print(result)





