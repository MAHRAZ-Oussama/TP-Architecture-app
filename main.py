from collections.abc import Iterable, Iterator


def add_grade4(cls):
    original_init = cls.__init__
    def new_init(self, name, grade1, grade2, grade3, grade4=0):
        original_init(self, name, grade1, grade2, grade3)
        self.grade4 = grade4
    cls.__init__ = new_init
    return cls


@add_grade4
class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3


class StudentIterator(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade1, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class StudentIterator2(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade2, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class StudentIterator3(Iterator):
    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.grade3, reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return StudentIterator(self.students)

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
school_class.add_student(Student('J', 10, 12, 13, 15))
school_class.add_student(Student('A', 8, 2, 17, 11))
school_class.add_student(Student('V', 9, 14, 14, 18))
school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()

for student in school_class:
    print(student.name, student.grade1)

for student in StudentIterator2(school_class.students):
    print(student.name, student.grade2)

for student in StudentIterator3(school_class.students):
    print(student.name, student.grade3)

for student in school_class.students:
    print(student.name, student.grade4)
