def collect_com(item, journal):
    if item not in journal:
        journal.append(item)
    return journal


def drop_com(item, journal):
    if item in journal:
        journal.remove(item)
    return journal


def combine_com(item_1, item_2, journal):
    for n in range(len(journal)):
        if journal[n] == item_1:
            journal.insert((n+1), item_2)
    return journal


def renew_com(item, journal):
    if item in journal:
        journal.append(item)
        journal.remove(item)
    return journal


inventory = input().split(', ')

command = input().split(' - ')

while not command[0] == 'Craft!':
    if 'Collect' in command:
        collect_com(command[1], inventory)
    elif 'Drop' in command:
        drop_com(command[1], inventory)
    elif 'Combine Items' in command:
        items = command[1].split(':')
        combine_com(items[0], items[1], inventory)
    elif 'Renew' in command:
        renew_com(command[1], inventory)
    command = input().split(' - ')

print(', '.join(inventory))