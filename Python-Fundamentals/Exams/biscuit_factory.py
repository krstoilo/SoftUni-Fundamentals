import math

b_per_day = int(input())
workers = int(input())
competition_30_days = int(input())

total_per_day = b_per_day*workers
total_b = 0

for n in range(30):
    if n % 3 == 0:
        total_b += 0.75 * total_per_day
    else:
        total_b += total_per_day

total_biscuits = math.floor(total_b)
print(f"You have produced {total_biscuits} biscuits for the past month.")

percentage = (100 * total_biscuits)/competition_30_days

if total_biscuits > competition_30_days:

    print(f'You produce {100 - percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {100 - percentage:.2f} percent less biscuits.')
