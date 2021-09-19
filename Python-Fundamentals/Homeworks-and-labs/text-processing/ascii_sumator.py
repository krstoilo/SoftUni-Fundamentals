start_symbol = ord(input())
end_symbol = ord(input())
test_string = input()
sum_of_chars = 0

for char in test_string:
    if start_symbol < ord(char) < end_symbol:
        sum_of_chars += ord(char)
print(sum_of_chars)