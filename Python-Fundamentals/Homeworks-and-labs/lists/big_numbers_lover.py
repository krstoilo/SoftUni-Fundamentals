line_of_nums = input().split()

line_of_nums.sort()
line_of_nums = line_of_nums[::-1]

print(''.join(line_of_nums))

