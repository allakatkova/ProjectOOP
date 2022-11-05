class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.name = name
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка!'


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass


if __name__ == '__main__':
    some_student = Student('Иван', 'Сидоров', 'мужской')
    some_student.finished_courses += ['Git']
    some_student.courses_in_progress += ['Python']
    some_student.grades['Git'] = [10, 10, 10, 10, 10]
    some_student.grades['Python'] = [10, 10]

    print(f"Фамилия {some_student.surname}, имя {some_student.name}, пол {some_student.gender}")
    print(f"Пройденные курсы {some_student.finished_courses}")
    print(f"Изучаемые курсы {some_student.courses_in_progress}")
    print(f"Оценки {some_student.grades}")

    print()

    some_student.add_courses('F#')
    print(f"Изучаемые курсы {some_student.finished_courses}")

    print()

    mentor_C = Mentor('Константин', 'Павловский')
    mentor_C.courses_attached.append('C#')
    mentor_P = Mentor('Владимир', 'Аркадьев')
    mentor_P.courses_attached.append('Python')

    print(mentor_C.name)
    print(mentor_C.surname)
    print(mentor_C.courses_attached)
    print(mentor_P.name)
    print(mentor_P.surname)
    print(mentor_P.courses_attached)

    print()

    some_student.courses_in_progress += ['C#']
    mentor_C.rate_hw(some_student, 'C#', 10)
    mentor_P.rate_hw(some_student, 'Python', 10)

    print(f"Фамилия {some_student.surname}, имя {some_student.name}, пол {some_student.gender}")
    print(f"Пройденные курсы {some_student.finished_courses}")
    print(f"Изучаемые курсы {some_student.courses_in_progress}")
    print(f"Оценки {some_student.grades}")
