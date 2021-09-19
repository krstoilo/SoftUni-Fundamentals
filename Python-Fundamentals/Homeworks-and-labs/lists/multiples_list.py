factor = int(input())
count = int(input())
my_list = []

for elem in range(1, count+1):
    my_list.append(factor*elem)

print(my_list)