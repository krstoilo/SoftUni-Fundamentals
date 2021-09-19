int_n = int(input())


def dec_to_binary(num):
    return bin(num).replace("0b", "")


binary_rep = dec_to_binary(int_n)
bit = binary_rep[-2]
print(int(bit) & 1)



