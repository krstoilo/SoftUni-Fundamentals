import re

text = input()
days = 0
total_calories = 0
final_list_of_food = []


def turn_to_str(tuple_list):
    string_list = []
    for n in range(len(tuple_list)):
        temp_str = "".join(tuple_list[n])
        string_list.append(temp_str)
    return string_list


regex = r'(#|\|)([A-Za-z ]+)(\1)([0-9]{2}/[0-9]{2}/[0-9]{2})(\1)([0-9]+)(\1)'
food_raw_info = re.findall(regex, text)

if len(food_raw_info) != 0:
    food_strings = turn_to_str(food_raw_info)
    for n in range(len(food_strings)):
        food_type = []
        if food_strings[n][0] == "#":
            token = food_strings[n].split("#")
            while "" in token:
                token.remove("")
            food = token[0]
            date = token[1]
            calories = token[2]
            food_type.append(food)
            food_type.append(date)
            food_type.append(calories)
            total_calories += int(calories)
        elif food_strings[n][0] == "|":
            token = food_strings[n].split("|")
            while "" in token:
                token.remove("")
            food = token[0]
            date = token[1]
            calories = token[2]
            food_type.append(food)
            food_type.append(date)
            food_type.append(calories)
            total_calories += int(calories)
        final_list_of_food.append(food_type)
        days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
if len(final_list_of_food) > 0:
    for n in range(len(final_list_of_food)):
        print(f'Item: {final_list_of_food[n][0]}, Best before: {final_list_of_food[n][1]}, '
              f'Nutrition: {final_list_of_food[n][2]}')

