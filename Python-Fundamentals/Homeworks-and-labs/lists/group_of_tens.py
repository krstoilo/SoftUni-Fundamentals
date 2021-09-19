list_of_nums = input().split(', ')
list_of_nums = [int(i) for i in list_of_nums]
group_boundary = 10

while len(list_of_nums) > 0:

    group = list(filter((lambda x: x <= group_boundary), list_of_nums))
    print(f"Group of {group_boundary}'s: {group}")
    list_of_nums = [x for x in list_of_nums if x not in group]
    group_boundary += 10
