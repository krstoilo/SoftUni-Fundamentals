courses = {}

command = input()
while command != 'end':
    command = command.split(" : ")
    if command[0] not in courses:
        courses[command[0]] = []
        courses[command[0]].append(command[1])
    else:
        courses[command[0]].append(command[1])
    command = input()

sorted_courses = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)

for (course, students) in sorted_courses:
    print(f"{course}: {len(students)}")
    students.sort()
    for i in range(len(students)):
        print(f" -- {students[i]}")




