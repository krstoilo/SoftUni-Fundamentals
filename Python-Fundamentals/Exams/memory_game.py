def clear_elements(list_sequence, element):
    list_sequence = [i for i in list_sequence if i != element]
    return list_sequence


sequence = input().split()
moves = 0
command_input = input()
while command_input != "end":
    command_input = command_input.split()
    moves += 1
    if command_input[0] == command_input[1] or 0 > int(command_input[1]) or 0 > int(command_input[0]) \
            or len(sequence) <= int(command_input[1]) or len(sequence) <= int(command_input[0]):
        print(f"Invalid input! Adding additional elements to the board")
        index_to_insert = len(sequence) // 2
        sequence.insert(index_to_insert, f"-{moves}a")
        sequence.insert(index_to_insert, f"-{moves}a")
    elif sequence[int(command_input[0])] == sequence[int(command_input[1])]:
        print(f"Congrats! You have found matching elements - {sequence[int(command_input[1])]}!")
        sequence = clear_elements(sequence, sequence[int(command_input[1])])
    elif sequence[int(command_input[0])] != sequence[int(command_input[1])]:
        print("Try again!")
    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break
    command_input = input()

if len(sequence) > 0:
    print(f"Sorry you lose :(\n"
          f"{' '.join(sequence)}")