fires = input().split('#')
water = int(input())
effort = 0
total_fire = 0
cells_list = []
isValid = False
cell_num = ""

for i in range(len(fires)):

    test_str = fires[i]

    for char in test_str:
        if char.isdigit() == True or char == '-':
            cell_num += char
    if 'High' in test_str:
        if 81 <= int(cell_num) <= 125:
            isValid = True
    elif 'Medium' in test_str:
        if 51 <= int(cell_num) <= 80:
            isValid = True
    elif 'Low' in test_str:
        if 1 <= int(cell_num) <= 50:
            isValid = True

    if isValid:
        if water >= int(cell_num):
            water -= int(cell_num)
            effort += 0.25 * int(cell_num)
            total_fire += int(cell_num)
            cells_list.append(cell_num)

    cell_num = ""
    isValid = False

print('Cells:')
for cell in range(len(cells_list)):
    print(f' - {cells_list[cell]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
