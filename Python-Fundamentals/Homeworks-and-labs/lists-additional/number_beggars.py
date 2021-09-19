sums_for_taking = [int(i) for i in input().split(", ")]
beggar_count = int(input())
beggar_sums = [0] * beggar_count

if beggar_count >= len(sums_for_taking):
    for n in range(len(sums_for_taking)):
        beggar_sums[n] = sums_for_taking[n]
else:
    for beggar in range(beggar_count):
        for turns in range(beggar, len(sums_for_taking), beggar_count):
            beggar_sums[beggar] += sums_for_taking[turns]

print(beggar_sums)