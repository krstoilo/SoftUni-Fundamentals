def sum_of_even_and_odd(number):
    current_digit = 0
    sum_even = 0
    sum_odd = 0
    while number > 0:
        current_digit = number % 10
        if current_digit % 2 == 0:
            sum_even += current_digit
        else:
            sum_odd += current_digit

        number = number // 10

    print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')


num = int(input())
sum_of_even_and_odd(num)