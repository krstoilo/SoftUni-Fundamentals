contests = {}
users = {}
total = {}

command = input()
while command != 'end of contests':
    token = command.split(":")
    contest = token[0]
    password = token[1]
    contests[contest] = password
    command = input()

participant = input()
while participant != 'end of submissions':
    token = participant.split("=>")
    contest = token[0]
    password = token[1]
    user = token[2]
    points = int(token[3])
    if contest in contests and contests[contest] == password:
        if user not in users:
            users[user] = []
            users[user].append([contest, points])
        if user not in total:
            total[user] = 0
            total[user] = points
        else:
            if users[user][0][0] == contest:
                if users[user][0][1] <= points:
                    total[user] -= users[user][0][1]
                    users[user][0][1] = points
            else:
                users[user].append([contest, points])
                total[user] += points
    participant = input()

sorted_total = sorted(total.items(), key=lambda x: [1], reverse=True)
sorted_users = sorted(users.items(), key=lambda x: x[0])

for (us, score) in total.items():
    print(f"Best candidate is {us} with total {score} points.")
    break
print("Ranking:")
for (name, submissions) in sorted_users:
    print(name)
    sorted_submission = sorted(submissions, key=lambda x: -x[1])
    for n in sorted_submission:
        print(f"#  {n[0]} -> {n[1]}")

