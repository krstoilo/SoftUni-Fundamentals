int_n = int(input())
p = int(input())


def dec_to_binary(num):
    return bin(num).replace("0b", "")


binary_rep = dec_to_binary(int_n)
if (p+1) >= len(binary_rep):
    bit = 0
else:
    bit = binary_rep[-(p+1)]
print(int(bit) & 1)