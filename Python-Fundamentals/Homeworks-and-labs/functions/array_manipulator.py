import sys


def define_count(input_command):
    count_index = ""
    for char in input_command:
        if char.isdigit():
            count_index += char
    count_index = int(count_index)
    return count_index


def exchange(given_index, array):
    first_list = []
    second_list = []
    for i in range(given_index + 1):
        first_list.append(array[i])
    for k in range(given_index + 1, len(array)):
        second_list.append(array[k])
    array = second_list + first_list
    return array


def max_even(array):
    max_even_num = -sys.maxsize
    index_max_even = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            if array[i] >= max_even_num:
                max_even_num = array[i]
                index_max_even = i
    if max_even_num < 0:
        return -1
    else:
        return index_max_even


def min_even(array):
    min_even_num = sys.maxsize
    index_min_even = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            if array[i] <= min_even_num:
                min_even_num = array[i]
                index_min_even = i
    if min_even_num >= sys.maxsize:
        return -1
    else:
        return index_min_even


def max_odd(array):
    max_odd_num = -sys.maxsize
    index_max_odd = 0
    for i in range(len(array)):
        if array[i] % 2 != 0:
            if array[i] >= max_odd_num:
                max_odd_num = array[i]
                index_max_odd = i
    if max_odd_num < 0:
        return -1
    else:
        return index_max_odd


def min_odd(array):
    min_odd_num = sys.maxsize
    index_min_odd = 0
    for i in range(len(array)):
        if array[i] % 2 != 0:
            if array[i] <= min_odd_num:
                min_odd_num = array[i]
                index_min_odd = i
    if min_odd_num >= sys.maxsize:
        return -1
    else:
        return index_min_odd


def first_even(count_first, array):
    even_array = []
    needed_count_array = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_array.append(array[i])
    if count_first > len(even_array):
        count_first = len(even_array)
    for n in range(count_first):
        needed_count_array.append(even_array[n])
    return needed_count_array


def first_odd(count_f_odd, array):
    odd_array = []
    needed_count_array = []
    for i in range(len(array)):
        if array[i] % 2 != 0:
            odd_array.append(array[i])
    if count_f_odd > len(odd_array):
        count_f_odd = len(odd_array)
    for n in range(count_f_odd):
        needed_count_array.append(odd_array[n])
    return needed_count_array


def last_even(count_last, array):
    even_array = []
    needed_count_array = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_array.append(array[i])
    if count_last > len(even_array):
        count_last = len(even_array)
    for n in range((len(even_array) - count_last), len(even_array)):
        needed_count_array.append(even_array[n])
    return needed_count_array


def last_odd(count_l_odd, array):
    odd_array = []
    needed_count_array = []
    for i in range(len(array)):
        if array[i] % 2 != 0:
            odd_array.append(array[i])
    if count_l_odd > len(odd_array):
        count_l_odd = len(odd_array)
    for n in range((len(odd_array) - count_l_odd), len(odd_array)):
        needed_count_array.append(odd_array[n])
    return needed_count_array


given_input = [int(i) for i in input().split(" ")]
command = input()

while command != "end":
    if "exchange" in command:
        count = define_count(command)
        if count >= len(given_input):
            print("Invalid index")
        else:
            changed_input = exchange(count, given_input)
            # print(changed_input)
            given_input = changed_input
    elif command == "max even":
        index = max_even(given_input)
        if index < 0:
            print("No matches")
        else:
            print(index)
    elif command == "max odd":
        index = max_odd(given_input)
        if index < 0:
            print("No matches")
        else:
            print(index)
    elif command == "min even":
        index = min_even(given_input)
        if index < 0:
            print("No matches")
        else:
            print(index)
    elif command == "min odd":
        index = min_odd(given_input)
        if index < 0:
            print("No matches")
        else:
            print(index)
    elif "first" in command:
        count = define_count(command)
        if count > len(given_input):
            print("Invalid count")
        else:
            if "even" in command:
                print(first_even(count, given_input))
            elif "odd" in command:
                print(first_odd(count, given_input))
    elif "last" in command:
        count = define_count(command)
        if count > len(given_input):
            print("Invalid count")
        else:
            if "even" in command:
                print(last_even(count, given_input))
            elif "odd" in command:
                print(last_odd(count, given_input))
    command = input()

print(given_input)
