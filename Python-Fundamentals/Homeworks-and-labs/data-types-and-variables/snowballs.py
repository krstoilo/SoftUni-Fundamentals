import sys

n = int(input())
snowball_value = -sys.maxsize
best_time = 0
best_snow = 0
best_quality = 0

for i in range(1, n+1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    current_value = (snowball_snow / snowball_time) ** snowball_quality

    if current_value >= snowball_value:
        snowball_value = current_value
        best_snow = snowball_snow
        best_time = snowball_time
        best_quality = snowball_quality

print(f'{best_snow} : {best_time} = {snowball_value:.0f} ({best_quality})')