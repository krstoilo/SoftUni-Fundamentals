empl_1_count = int(input())
empl_2_count = int(input())
empl_3_count = int(input())

total_processed = empl_1_count+empl_2_count+empl_3_count

total_people = int(input())

hours = 0

while total_people > 0:
    total_people -= total_processed
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

