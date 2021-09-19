shopping_list = input().split("!")

command = input()

while command != "Go Shopping!":
    if "Urgent" in command:
        command = command.split()
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])
    elif "Unnecessary" in command:
        command = command.split()
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    elif "Correct" in command:
        command = command.split()
        if command[1] in shopping_list:
            shopping_list = [command[2] if x == command[1] else x for x in shopping_list]
    elif "Rearrange" in command:
        command = command.split()
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])
    command = input()

print(", ".join(shopping_list))