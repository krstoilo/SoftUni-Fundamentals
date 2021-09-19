sequence = [int(i) for i in input().split()]

average = 0
top_five = []

for n in range(len(sequence)):
    average += sequence[n]
average = average // len(sequence)
for el in sequence:
    if el > average:
        top_five.append(el)
if len(top_five) < 1:
    print("No")
else:
    top_five.sort(reverse=True)
    top_five = top_five[0:5]
    top_five = [str(i) for i in top_five]
    print(' '.join(top_five))