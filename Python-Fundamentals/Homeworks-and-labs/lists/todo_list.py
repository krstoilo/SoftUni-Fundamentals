command = input()
notes = [0] * 10

while not command == "End":
    command = command.split("-")
    importance = int(command[0])
    note = command[1]
    notes.insert(importance, note)
    command = input()

result = [el for el in notes if el != 0]
print(result)