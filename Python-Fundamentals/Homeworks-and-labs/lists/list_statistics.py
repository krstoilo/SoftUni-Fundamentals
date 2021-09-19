n = int(input())

positives = []
negatives = []
pos_count = 0
neg_sum = 0

for i in range(1, n+1):
    number = int(input())
    if number >= 0:
        pos_count += 1
        positives.append(number)
    else:
        neg_sum += number
        negatives.append(number)

print(positives)
print(negatives)
print(f'Count of positives: {pos_count}. Sum of negatives: {neg_sum}')