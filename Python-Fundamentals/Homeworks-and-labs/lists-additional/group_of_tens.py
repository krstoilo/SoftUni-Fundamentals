number_list = [int(i) for i in input().split(", ")]
group_bound = 10

while number_list:
    numbers_in_group = [i for i in number_list if i <= group_bound]
    number_list = [j for j in number_list if j > group_bound]
    print(f"Group of {group_bound}'s: {numbers_in_group}")
    group_bound += 10


