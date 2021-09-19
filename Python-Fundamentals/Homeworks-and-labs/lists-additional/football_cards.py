cards_sequence = input().split()
cards_sequence = list(dict.fromkeys(cards_sequence))

team_A = 11
team_B = 11

for card in cards_sequence:
    if 'A' in card:
        team_A -= 1
    elif 'B' in card:
        team_B -= 1
    if team_A < 7 or team_B < 7:
        break

print(f'Team A - {team_A}; Team B - {team_B}')
if team_B < 7 or team_A < 7:
    print("Game was terminated")