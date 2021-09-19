contests = {}
users = {}

command = input()
while command != 'no more time':
    token = command.split(" -> ")
    username = token[0]
    contest = token[1]
    points = int(token[2])
    if contest not in contests:
        contests[contest] = {username: points}
    else:
        if username in contests[contest]:
            if username in users:
                users[username] -= contests[contest][username]
                contests[contest][username] = points
        contests[contest][username] = points
    if username not in users:
        users[username] = 0
        users[username] += points
    else:
        users[username] += points
    command = input()

for (key, value) in contests.items():
    print(f"{key}: {len(value)} participants")
    for count, (k, v) in enumerate(sorted(value.items(), key=lambda x: -x[1]),start=1):
        print(f"{count}. {k} <::> {v}")

sorted_users = sorted(users.items(), key=lambda x: -x[1])
print("Individual standings:")
for count, (key, value) in enumerate(sorted_users, start=1):
    print(f"{count}. {key} -> {value}")
