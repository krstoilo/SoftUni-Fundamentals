tier = {}

command = input()
while command != "Season end":
    if "->" in command:
        token = command.split(" -> ")
        player = token[0]
        position = token[1]
        skill = int(token[2])
        if player not in tier:
            tier[player] = {}
            tier[player][position] = skill
        else:
            if position not in tier[player]:
                tier[player][position] = skill
            else:
                if tier[player][position] < skill:
                    tier[player][position] = skill
    else:
        token = command.split(" vs ")
        player1 = token[0]
        player2 = token[1]
        if player2 in tier and player1 in tier:
            for key in tier[player1].keys():
                if key in tier[player2].keys():
                    if tier[player1][key] > tier[player2][key]:
                        del tier[player2]
                        break
                    elif tier[player1][key] < tier[player2][key]:
                        del tier[player1]
                        break
    command = input()

print(tier.items())

for player, totalSkill in sorted(tier.items(), key=lambda x: (-sum(i for i in x[1].values()), x[0])):
    print(f'{player}: {sum(totalSkill.values())} skill')
    for user, skill in sorted(tier[player].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {user} <::> {skill}')