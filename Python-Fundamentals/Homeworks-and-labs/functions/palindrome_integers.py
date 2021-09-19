input_integers = [int(i) for i in input().split(", ")]


def check_palindrome(integer_list):
    for num in integer_list:
        str_num = str(num)
        if str_num[::] == str_num[::-1]:
            print("True")
        else:
            print("False")


check_palindrome(input_integers)
