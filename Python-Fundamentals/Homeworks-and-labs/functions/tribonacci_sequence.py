def print_trib_rec(num):

    if num == 1 or num == 2:
        return 1
    elif num == 3:
        return 2
    else:
        return (print_trib_rec(num - 1) +
                print_trib_rec(num - 2) +
                print_trib_rec(num - 3))


def print_trib(n):
    for i in range(1, n+1):
        print(print_trib_rec(i), end=" ")


num = int(input())
print_trib(num)
