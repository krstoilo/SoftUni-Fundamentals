current_version = input().split('.')
current_version = [int(i) for i in current_version]

new_version = []

if current_version[2] < 9:
    new_version.append(current_version[2]+1)
    new_version.insert(0, current_version[1])
    new_version.insert(0, current_version[0])
else:
    new_version.insert(0, 0)
    if current_version[1] < 9:
        new_version.insert(0, current_version[1] + 1)
        new_version.insert(0, current_version[0])
    else:
        new_version.insert(0, 0)
        if current_version[0] < 9:
            new_version.insert(0, current_version[0] + 1)
        else:
            new_version.insert(0, 0)

new_version = [str(i) for i in new_version]
print('.'.join(new_version))