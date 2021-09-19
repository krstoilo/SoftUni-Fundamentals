num1 = int(input())
num2 = int(input())
num3 = int(input())

def determine_sign(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        print("zero")
    elif num1 > 0 and num2 > 0 and num3 > 0:
        print("positive")
    elif num1 > 0 > num3 and num2 > 0:
        print("negative")
    elif num2 > 0 > num1 and num3 > 0:
        print("negative")
    elif num1 > 0 > num2 and num3 > 0:
        print("negative")
    elif num1 < 0 and num2 < 0 and num3 < 0:
        print("negative")
    else:
        print("positive")


determine_sign(num1, num2, num3)