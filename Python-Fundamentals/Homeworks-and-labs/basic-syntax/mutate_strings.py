first_str = input()
second_str = input()

previous_str = ""
new_str = ""

for iteration in range(len(first_str)):
    for index_string_2 in range(0, iteration+1):
        new_str += second_str[index_string_2]
    for index_string_1 in range(iteration+1, len(first_str)):
        new_str += first_str[index_string_1]
    if previous_str != new_str:
        print(new_str)
    previous_str = new_str
    new_str = ""