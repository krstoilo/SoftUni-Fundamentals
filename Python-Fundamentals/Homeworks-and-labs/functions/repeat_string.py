string_input = input()
n = int(input())


def repeat_string(text, number):
    result = ""
    for times in range(n):
        result += text
    return result


print(repeat_string(string_input, n))
