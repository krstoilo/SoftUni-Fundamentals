number_of_people = int(input())
elevator_capacity = int(input())
courses = 0

while number_of_people > 0:
    if number_of_people > elevator_capacity:
        number_of_people -= elevator_capacity
        courses += 1
    else:
        courses += 1
        break

print(courses)