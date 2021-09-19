number = int(input())
is_prime = False

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            break
        else:
            is_prime = True

print(is_prime)