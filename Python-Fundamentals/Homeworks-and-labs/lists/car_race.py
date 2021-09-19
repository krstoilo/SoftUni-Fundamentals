race = [int(i) for i in input().split()]

racer_elements = int((len(race) - 1)/2)

left_car = race[0:racer_elements]
right_car = race[(racer_elements + 1):]

left_car_time = 0
right_car_time = 0

for elem in left_car:
    if elem == 0:
        left_car_time *= 0.8
    else:
        left_car_time += elem

for elem in right_car:
    if elem == 0:
        right_car_time *= 0.8
    else:
        right_car_time += elem

if left_car_time <= right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")