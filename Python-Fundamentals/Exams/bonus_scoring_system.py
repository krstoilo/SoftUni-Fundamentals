import math

enrolled_students = int(input())
all_lectures = int(input())
additional_bonus = int(input())

student_records = []
best_score = 0
total_attendance = 0

for n in range(enrolled_students):
    student_attendance = int(input())
    total_bonus = student_attendance / all_lectures * (5 + additional_bonus)
    if total_bonus > best_score:
        best_score = total_bonus
        total_attendance = student_attendance

print(f"Max Bonus: {math.ceil(best_score)}.\n"
      f"The student has attended {total_attendance} lectures.")
