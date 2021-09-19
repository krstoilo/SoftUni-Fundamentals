operator = input()
int1 = int(input())
int2 = int(input())


def calculate(int1, int2, oper):
    result = None
    if oper == 'multiply':
        result = int1 * int2
    elif oper == 'divide':
        if int2 is not 0:
            result = int(int1 / int2)
        else:
            print("WRONG")
    elif oper == 'add':
        result = int1 + int2
    else:
        result = int1 - int2

    return result


print(calculate(int1, int2, operator))
