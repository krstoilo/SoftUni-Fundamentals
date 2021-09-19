number = input()


def sum_even_and_odd_digits(num):
    even_sum = 0
    odd_sum = 0
    for n in range(len(num)):
        if int(num[n]) % 2 == 0:
            even_sum += int(num[n])
        else:
            odd_sum += int(num[n])
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(sum_even_and_odd_digits(number))