current_version = input().split(".")
next_version = []

if int(current_version[2]) < 9:
    next_version.append(current_version[0])
    next_version.append(current_version[1])
    next_version.append(str(int(current_version[2])+1))
elif int(current_version[2]) == 9:
    if int(current_version[1]) < 9:
        next_version.append(current_version[0])
        next_version.append(str(int(current_version[1]) + 1))
        next_version.append('0')
    elif int(current_version[1]) == 9:
        next_version.append(str(int(current_version[0])+1))
        next_version.append('0')
        next_version.append('0')

print('.'.join(next_version))