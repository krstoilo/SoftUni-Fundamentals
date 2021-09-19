electrons = int(input())
shells = []
n = 1
while electrons > 0:
    shell_electrons = 2 * (n**2)
    if electrons - shell_electrons > 0:
        electrons -= shell_electrons
        shells.append(shell_electrons)
    else:
        shells.append(electrons)
        electrons -= electrons
    n += 1

print(shells)