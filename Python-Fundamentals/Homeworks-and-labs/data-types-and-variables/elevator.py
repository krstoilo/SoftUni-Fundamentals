persons_n = int(input())
elevator_capacity_p = int(input())

courses = persons_n/elevator_capacity_p
if persons_n % elevator_capacity_p != 0:
    courses += 1

print(int(courses))