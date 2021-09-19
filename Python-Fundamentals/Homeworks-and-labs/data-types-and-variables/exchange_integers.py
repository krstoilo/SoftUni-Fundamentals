int_a = int(input())
int_b = int(input())

temp_int = int_a
int_a = int_b
int_b = temp_int

print(f'Before:')
print(f'a = {int_b}')
print(f'b = {int_a}')
print(f'After:')
print(f'a = {int_a}')
print(f'b = {int_b}')