class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average = 0
        for i in range(len(self.grades)):
            average += float(self.grades[i])
        return f'{average/len(self.students):.2f}'

    def __repr__(self):
        students = ', '.join(self.students)
        return f"The students in {self.name}: {students}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Amy", 3.50)
a_class.add_student("George", 6.00)
a_class.add_student("Mila", 5.80)
a_class.add_student("Niko", 4.40)
print(a_class)