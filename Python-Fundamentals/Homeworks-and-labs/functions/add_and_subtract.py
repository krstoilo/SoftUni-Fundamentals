num1 = int(input())
num2 = int(input())
num3 = int(input())


def sum_numbers(number1, number2):
    return number1 + number2


def subtract(result, number3):
    return result - number3


def add_and_subtract(n1, n2, n3):
    return subtract(sum_numbers(n1, n2), n3)


print(add_and_subtract(num1, num2, num3))