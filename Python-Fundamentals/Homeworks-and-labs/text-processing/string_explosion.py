user_input = input()   #abv>1>1>2>2asdasd
exploded_str = user_input

for n in range(len(user_input)):
    explosion_strength = 0
    if user_input[n] == ">":
        explosion_strength += int(user_input[n+1])
        if user_input[n+explosion_strength] != ">":
            exploded_str = user_input[:n] + user_input[n+explosion_strength+1:]
            user_input = exploded_str
        else:
            explosion_strength += user_input[n+explosion_strength+1]