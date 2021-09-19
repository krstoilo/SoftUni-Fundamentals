int_n = int(input())
p = int(input())
mask = ~(1 << p)
bit = int_n & mask
print(bit)

