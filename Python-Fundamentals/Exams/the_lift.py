queue = int(input())
lift_wagons = [int(i) for i in input().split()]


def is_full(wagons):
    result = [all(elem == 4 for elem in wagons)]
    return result


while queue >= 0:
    for n in range(len(lift_wagons)):
        while lift_wagons[n] < 4 and queue > 0:
            queue -= 1
            lift_wagons[n] += 1
    if is_full(lift_wagons):
        break

lift_wagons = [str(i) for i in lift_wagons]

if is_full(lift_wagons) and queue == 0:
    print(f"The lift has empty spots!")
elif queue > 0 and is_full(lift_wagons):
    print(f"There isn't enough space! {queue} people in a queue!")
print(f"{' '.join(lift_wagons)}")
