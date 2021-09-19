def calc_factorial(number):
    factorial = 1
    if number < 0:
        return -1
    elif number == 0:
        return 1
    else:
        for n in range(1, number+1):
            factorial = factorial * n
        return factorial


num1 = int(input())
num2 = int(input())

fac_num1 = calc_factorial(num1)
fac_num2 = calc_factorial(num2)

if fac_num2 < 0 or fac_num1 < 0:
    print("Error")
else:
    print(f'{fac_num1/fac_num2:.2f}')
