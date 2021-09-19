password_input = input()
password = password_input

command = input()
while command != 'Done':
    if "TakeOdd" in command:
        temp_pass = ""
        for n in range(len(password)):
            if n % 2 == 1:
                temp_pass += password[n]
        password = temp_pass
        print(password)
    elif "Cut" in command:
        token = command.split()
        index = int(token[1])
        length = int(token[2])
        temp_pass = password[:index] + password[index+length:]
        password = temp_pass
        print(password)
    elif "Substitute" in command:
        token = command.split()
        substring = token[1]
        substitute = token[2]
        if substring in password:
            temp_pass = password.replace(substring, substitute)
            password = temp_pass
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f'Your password is: {password}')