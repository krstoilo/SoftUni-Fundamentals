sides = {}

command = input()
while command != 'Lumpawaroo':
    if "|" in command:
        token = command.split(" | ")
        user = token[1]
        side = token[0]
        if side not in sides:
            sides[side] = []
            sides[side].append(user)
        else:
            if user not in sides[side]:
                sides[side].append(user)
    elif "->" in command:
        token = command.split(" -> ")
        user = token[0]
        side = token[1]
        for (key, value) in sides.items():
            if user in value:
                value.remove(user)
                break
        if side not in sides:
            sides[side] = []
            sides[side].append(user)
        else:
            sides[side].append(user)
        print(f"{user} joins the {side} side!")
    command = input()


sorted_side = sorted(sides.items(), key=lambda x: (-len(x[1]), x[0]))

for (side, users) in sorted_side:
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")