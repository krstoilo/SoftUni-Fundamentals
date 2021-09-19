row_1 = input().split()
row_2 = input().split()
row_3 = input().split()

player_1_won = False
player_2_won = False

for i in range(len(row_3)):
    if row_1[i] == row_2[i] == row_3[i] == '1':
        player_1_won = True
    elif row_1[i] == row_2[i] == row_3[i] == '2':
        player_2_won = True

if row_1[0] == row_1[1] == row_1[2] == '1':
    player_1_won = True
if row_2[0] == row_2[1] == row_2[2] == '1':
    player_1_won = True
if row_3[0] == row_3[1] == row_3[2] == '1':
    player_1_won = True

if row_1[0] == row_1[1] == row_1[2] == '2':
    player_2_won = True
if row_2[0] == row_2[1] == row_2[2] == '2':
    player_2_won = True
if row_3[0] == row_3[1] == row_3[2] == '2':
    player_2_won = True

if row_1[0] == row_2[1] == row_3[2] == '1':
    player_1_won = True
if row_1[2] == row_2[1] == row_3[0] == '1':
    player_1_won = True

if row_1[0] == row_2[1] == row_3[2] == '2':
    player_2_won = True
if row_1[2] == row_2[1] == row_3[0] == '2':
    player_2_won = True

if player_1_won:
    print("First player won")
elif player_2_won:
    print("Second player won")
else:
    print("Draw!")