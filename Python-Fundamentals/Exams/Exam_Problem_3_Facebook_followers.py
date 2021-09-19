followers = {}

command = input()
while command != "Log out":
    if "New" in command:
        token = command.split(": ")
        username = token[1]
        if username in followers:
            pass
        else:
            details = [0,0,0]
            followers[username] = details
    elif "Like" in command:
        token = command.split(": ")
        username = token[1]
        count = int(token[2])
        if username in followers:
            followers[username][0] = count
        else:
            details = [count, 0, 0]
            followers[username] = details
    elif "Comment" in command:
        token = command.split(": ")
        username = token[1]
        if username in followers:
            followers[username][1] += 1
        else:
            details = [0, 1, 0]
            followers[username] = details
    elif "Blocked" in command:
        token = command.split(": ")
        username = token[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")
    command = input()


for fol in followers:
    followers[fol][2] = followers[fol][0] + followers[fol][1]


sorted_followers = dict(sorted(followers.items(),key= lambda x:(-x[1][2], x[0])))
print(f"{len(followers)} followers")
for follower, interactions in sorted_followers.items():
    print(f'{follower}: {interactions[2]}')