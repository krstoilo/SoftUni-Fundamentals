command = input()

dwarfs = {}

while command != 'Once upon a time':
    token = command.split(" <:> ")
    dwarf_name = token[0]
    hat_color = token[1]
    physics = int(token[2])
    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}
        dwarfs[hat_color][dwarf_name] = physics
    else:
        if dwarf_name not in dwarfs[hat_color]:
            dwarfs[hat_color][dwarf_name] = physics
        else:
            if physics > dwarfs[hat_color][dwarf_name]:
                dwarfs[hat_color][dwarf_name] = physics
    command = input()

# for color, name in sorted(dwarfs.items(), key=lambda x: -len(x[0])):
#     for n, phy in name.items():
#         print(f"({color}) {n} <-> {phy}")

sorted_dwarfs = sorted(dwarfs,key=lambda x: -dwarfs[dwarfs[0]][0])
print(sorted_dwarfs)