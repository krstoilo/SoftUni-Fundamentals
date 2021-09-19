import re

runners_dict = {}
participants = input().split(", ")

for name in participants:
    runners_dict[name] = 0

running_info = input()
pattern_name = r"([a-zA-Z]+)"
pattern_number = r"([0-9])"
while running_info != 'end of race':
    name_match = re.findall(pattern_name, running_info)
    number_match = re.findall(pattern_number, running_info)
    p_name = "".join(name_match)
    p_distance = sum(int(n) for n in number_match)
    if p_name in runners_dict:
        runners_dict[p_name] += p_distance
    running_info = input()

winners = list(sorted(runners_dict.items(), key=lambda x: -x[1]))
print(f'1st place: {winners[0][0]}')
print(f'2nd place: {winners[1][0]}')
print(f'3rd place: {winners[2][0]}')
