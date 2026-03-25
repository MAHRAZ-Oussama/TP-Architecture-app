class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.grade1, reverse=True)
        for student in sorted_students:
            print(student.name, student.grade1)

    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.grade2, reverse=True)
        for student in sorted_students:
            print(student.name, student.grade2)

    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.grade3, reverse=True)
        for student in sorted_students:
            print(student.name, student.grade3)


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))
school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()
