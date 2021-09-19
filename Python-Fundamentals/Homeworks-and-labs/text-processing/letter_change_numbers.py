user_input = input().split()
total_sum = 0

for string in user_input:
    num = ""
    for ch in string:
        if ch.isdigit():
            num += ch
    the_number = int(num)
    if string[0].islower():
        the_number *= (ord(string[0])-96)
    else:
        the_number /= (ord(string[0])-64)
    if string[-1].islower():
        the_number += (ord(string[-1])-96)
    else:
        the_number -= (ord(string[-1]) - 64)
    total_sum += the_number

print(f"{total_sum:.2f}")
