user_input = input().split()
word_1 = user_input[0]
word_2 = user_input[1]
total_sum = 0

if len(word_1) == len(word_2):
    for n in range(len(word_1)):
        total_sum += ord(word_1[n])*ord(word_2[n])
else:
    if len(word_1) > len(word_2):
        for n in range(len(word_2)):
            total_sum += ord(word_1[n]) * ord(word_2[n])
        for m in range(len(word_2), len(word_1)):
            total_sum += ord(word_1[m])
    else:
        for n in range(len(word_1)):
            total_sum += ord(word_1[n]) * ord(word_2[n])
        for m in range(len(word_1), len(word_2)):
            total_sum += ord(word_2[m])

print(total_sum)
