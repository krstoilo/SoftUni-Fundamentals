string = input()

list = string.split(", ")
sheep_number = 0

if list[len(list)-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    list.reverse()
    for elem in range(0,len(list)):
        if list[elem] == 'wolf':
            sheep_number = elem
    print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')
