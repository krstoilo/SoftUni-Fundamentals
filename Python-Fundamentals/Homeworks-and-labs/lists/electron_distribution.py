electrons = int(input())
shell = 1
shell_list = []

while True:
    if electrons >= 2*shell**2:
        shell_list.append(2*shell**2)
        electrons -= 2*shell**2
        shell += 1
    else:
        if not electrons == 0:
            shell_list.append(electrons)
            break
        else:
            break

print(shell_list)