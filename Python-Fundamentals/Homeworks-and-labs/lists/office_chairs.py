def record_number(input_string):
    number = ""
    for char in input_string:
        if char.isdigit():
            number += char
    return number


rooms_count = int(input())

free_chairs = 0
not_enough_chairs = False

for n in range(1, rooms_count+1):
    room_status = input().split()
    chairs = int(record_number(room_status[1]))

    if len(room_status[0]) < chairs:
        print(f'{chairs - len(room_status[0])} more chairs needed in room {n}')
        not_enough_chairs = True
    else:
        free_chairs += len(room_status[0]) - chairs

if not not_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")