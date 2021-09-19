password = input()


def check_pass(pass_word):
    length = False
    chars = False
    digits = False
    digit_count = 0
    if 6 <= len(pass_word) <= 10:
        length = True
        pass
    else:
        print("Password must be between 6 and 10 characters")
    for char in pass_word:
        if char.isdigit() or char.isalpha():
            chars = True
            pass
        else:
            print("Password must consist only of letters and digits")
            break
    for char in pass_word:
        if char.isdigit():
            digit_count += 1
    if digit_count >= 2:
        digits = True
        pass
    else:
        print("Password must have at least 2 digits")
    if length and chars and digits:
        print("Password is valid")


check_pass(password)