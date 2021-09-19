input_strings = input().split()
new_string = [i*len(i) for i in input_strings]
print(''.join(new_string))