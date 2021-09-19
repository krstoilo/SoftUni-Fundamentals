integer_input = int(input())
bin_digit = input()
d_counter = 0


def decimal_to_binary(num):
    return bin(num).replace("0b", "")


binary_num = decimal_to_binary(integer_input)

for e in binary_num:
    if e == bin_digit:
        d_counter += 1

print(d_counter)