def get_number(str_input):
    number = ""
    for char in str_input:
        if char.isdigit():
            number += char
    number = int(number)
    return number


wagons = int(input())

train = [0] * wagons

command = input()

while not command == "End":
    if "add" in command:
        added_people = get_number(command)
        train[-1] += added_people
    elif "insert" in command:
        command = command.split()
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif "leave" in command:
        command = command.split()
        index = int(command[1])
        people = int(command[2])
        train[index] -= people
    command = input()

print(train)