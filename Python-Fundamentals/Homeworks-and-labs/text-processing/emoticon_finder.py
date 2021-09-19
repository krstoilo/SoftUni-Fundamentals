user_input = input()
emoticons = []


for n in range(len(user_input)):
    if user_input[n] == ":":
        if user_input[n+1] != "." and user_input[n+1] != " ":
            emote = user_input[n] + user_input[n+1]
            emoticons.append(emote)

for elem in emoticons:
    print(elem)