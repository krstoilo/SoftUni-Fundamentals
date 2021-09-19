n = int(input())

student_grades = {}
remove_students = []


def calculate_average(students):
    average_grade = 0
    for j in range(len(students)):
        average_grade += students[j]
    return average_grade / len(students)


for i in range(n):
    student = input()
    grade = float(input())
    if student not in student_grades:
        student_grades[student] = []
        student_grades[student].append(grade)
    else:
        student_grades[student].append(grade)

for iteration in student_grades:
    student_grades[iteration] = calculate_average(student_grades[iteration])
    if student_grades[iteration] < 4.5:
        remove_students.append(iteration)

for student in remove_students:
    del student_grades[student]

sorted_students = sorted(student_grades.items(), key=lambda x: x[1], reverse=True)
for (student, grade) in sorted_students:
    print(f"{student} -> {grade:.2f}")