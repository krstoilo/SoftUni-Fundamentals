users = {}
submissions = {}

command = input()

while command != "exam finished":
    if 'banned' in command:
        token = command.split('-')
        user = token[0]
        del users[user]
    else:
        token = command.split('-')
        username = token[0]
        language = token[1]
        points = int(token[2])
        if username not in users:
            users[username] = points
        else:
            if points > users[username]:
                users[username] = points
        if language not in submissions:
            submissions[language] = 0
            submissions[language] += 1
        else:
            submissions[language] += 1
    command = input()

sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
sorted_submissions = sorted(submissions.items(), key=lambda x: (-x[1], x[0]))

print("Results:")
for (key, value) in sorted_users:
    print(f"{key} | {value}")
print("Submissions:")
for (language, count) in sorted_submissions:
    print(f"{language} - {count}")