n = int(input())
users = {}

for i in range(n):
    command = input().split()
    if 'register' in command:
        if command[1] not in users:
            users[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {users[command[1]]}")
    if 'unregister' in command:
        if command[1] in users:
            del users[command[1]]
            print(f"{command[1]} unregistered successfully")
        else:
            print(f"ERROR: user {command[1]} not found")

for (username, plate) in users.items():
    print(f"{username} => {plate}")