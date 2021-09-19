factor = int(input())
count = int(input())
i = 1
multiples = []
for n in range(count):
    multiples.append(factor*i)
    i += 1
print(multiples)