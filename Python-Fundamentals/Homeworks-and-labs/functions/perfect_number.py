number = int(input())


def perfection_check(num):
    if num > 0:
        sum_divisors = 0
        for i in range(1, int(num/2)+1):
            if num % i == 0:
                sum_divisors += i
        if sum_divisors == num:
            return True
        else:
            return False
    else:
        return False


if perfection_check(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")