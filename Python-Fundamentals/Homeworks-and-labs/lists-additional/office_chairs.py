rooms = int(input())
free_chairs = 0
vacant_chairs = True
for n in range(1, rooms+1):
    chairs = input().split()
    if len(chairs[0]) < int(chairs[1]):
        print(f'{int(chairs[1]) - len(chairs[0])} more chairs needed in room {n}')
        vacant_chairs = False
    else:
        free_chairs += len(chairs[0]) - int(chairs[1])

if vacant_chairs:
    print(f'Game On, {free_chairs} free chairs left')