command = input()
resources = {}


while command != "stop":
    if command not in resources:
        resources[command] = 0
    quantity = int(input())
    resources[command] += quantity
    command = input()

for (resource, count) in resources.items():
    print(f"{resource} -> {count}")
