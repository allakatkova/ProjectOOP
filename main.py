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

    @staticmethod
    def rate_hw_lecturer(lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка!'

    def __str__(self):
        result = (f"Имя: {self.name} \n" 
                  f"Фамилия: {self.surname} \n"
                  f"Средняя оценка за домашние задания: {self.__calc_average_score(self)} \n"
                  f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
                  f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return result

    @staticmethod
    def __calc_average_score(self):
        sum_elem = 0
        count = 0
        for elem in self.grades.values():
            for grade in elem:
                sum_elem += grade
                count += 1
        if count != 0:
            result = sum_elem/count
        else:
            result = 0
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Объект не принадлежит к классу Student")
            return
        return self.__calc_average_score(self) < other.__calc_average_score(other)


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.name = name
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        result = (f"Имя: {self.name} \n" 
                  f"Фамилия: {self.surname} \n"
                  f"Средняя оценка за лекции: {self.__calc_average_score(self)}")
        return result

    @staticmethod
    def __calc_average_score(self):
        sum_elem = 0
        count = 0
        for elem in self.grades.values():
            for grade in elem:
                sum_elem += grade
                count += 1
        if count != 0:
            result = sum_elem/count
        else:
            result = 0
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Объект не принадлежит к классу Lecturer")
            return
        return self.__calc_average_score(self) < other.__calc_average_score(other)


class Reviewer(Mentor):

    def rate_hw_student(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка!'

    def __str__(self):
        result = (f"Имя: {self.name} \n" 
                  f"Фамилия: {self.surname}")
        return result


def output_info_of_student(student):
    print(f"Студент {student.name} {student.surname}, пол {student.gender}")
    print(f"Пройденные курсы {student.finished_courses}")
    print(f"Изучаемые курсы {student.courses_in_progress}")
    print(f"Оценки {student.grades}")


def students_average_score_calculation(students_list, course):
    for student in students_list:
        sum_grades_course = 0
        count_grades = 0
        sum_average = 0
        if isinstance(student, Student) and course in student.grades:
            student_grades = student.grades[course]
            for grade in student_grades:
                sum_grades_course += grade
                count_grades += 1
            if count_grades != 0:
                sum_average = sum_grades_course / count_grades
            else:
                sum_average = 0
        else:
            result = 0
        result = (f"Имя: {student.name} \n"
                  f"Фамилия: {student.surname} \n"
                  f"Средняя оценка за ДЗ по {course}: {sum_average}\n")
        print(result)

def lecturers_average_score_calculation(lecturers_list, course):
    for lecturer in lecturers_list:
        sum_grades_course = 0
        count_grades = 0
        sum_average = 0
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            lecturer_grades = lecturer.grades[course]
            for grade in lecturer_grades:
                sum_grades_course += grade
                count_grades += 1
            if count_grades != 0:
                sum_average = sum_grades_course / count_grades
            else:
                sum_average = 0
        else:
            result = 0
        result = (f"Имя: {lecturer.name} \n"
                  f"Фамилия: {lecturer.surname} \n"
                  f"Средняя оценка за лекции по {course}: {sum_average}\n")
        print(result)


if __name__ == '__main__':

    print()
    print("------------Task 1------------")
    print()

    some_student = Student('Иван', 'Сидоров', 'мужской')
    some_student.finished_courses += ['Git']
    some_student.courses_in_progress += ['Python']
    some_student.grades['Git'] = [10, 6, 5, 8, 1]
    some_student.grades['Python'] = [10, 2]

    output_info_of_student(some_student)

    print()

    some_student.add_courses('F#')
    some_student.grades['F#'] = [10, 10, 10, 10, 10]
    print(f"Изучаемые курсы {some_student.finished_courses}")

    print()

    mentor_C = Reviewer('Константин', 'Павловский')
    mentor_C.courses_attached.append('C#')
    mentor_P = Reviewer('Владимир', 'Аркадьев')
    mentor_P.courses_attached.append('Python')

    print(f"Преподаватель {mentor_C.name} {mentor_C.surname}, "
          f"дисциплина {mentor_C.courses_attached}")
    print(f"Преподаватель {mentor_P.name} {mentor_P.surname}, "
          f"дисциплина {mentor_P.courses_attached}")

    print()

    some_student.courses_in_progress += ['C#']
    mentor_C.rate_hw_student(some_student, 'C#', 10)
    mentor_P.rate_hw_student(some_student, 'Python', 10)

    output_info_of_student(some_student)

    print()
    print("------------Task 2------------")
    print()

    lecturer_F = Lecturer("Герман", "Якубовский")
    lecturer_F.courses_attached += ['F#']
    lecturer_F.courses_attached += ['C#']
    print(f"Преподаватель {lecturer_F.name} {lecturer_F.surname}, "
          f"дисциплина {lecturer_F.courses_attached}")
    some_student.rate_hw_lecturer(lecturer_F, 'F#', 10)
    some_student.rate_hw_lecturer(lecturer_F, 'C#', 6)
    print(f"оценка {lecturer_F.grades}")

    lecturer_L = Lecturer("Семен", "Витаков")
    lecturer_L.courses_attached += ['Web']
    lecturer_L.courses_attached += ['Python']
    print(f"Преподаватель {lecturer_L.name} {lecturer_L.surname}, "
          f"дисциплина {lecturer_L.courses_attached}")

    some_student.rate_hw_lecturer(lecturer_L, 'Web', 8)
    some_student.rate_hw_lecturer(lecturer_L, 'Python', 9)
    some_student.rate_hw_lecturer(lecturer_L, 'Python', 4)
    some_student.rate_hw_lecturer(lecturer_L, 'Python', 3)
    print(f"оценка {lecturer_L.grades}")

    print()
    print("------------Task 3.1------------")
    print()

    print(mentor_C)
    print(mentor_P)

    print()

    print(lecturer_F)
    print(lecturer_L)

    print()

    print(lecturer_F < lecturer_L)

    print()
    print("------------Task 3.2------------")
    print()

    student_for_eval = Student('Петр', 'Вавилов', 'мужской')
    student_for_eval.courses_in_progress += ['Git']
    student_for_eval.grades['Git'] = [1, 2, 3, 4, 5]
    output_info_of_student(student_for_eval)

    print(some_student < student_for_eval)

    print()
    print("------------Task 4.1------------")
    print()

    students_average_score_calculation([some_student, student_for_eval], 'Python')
    students_average_score_calculation([some_student, student_for_eval], 'Git')

    print()
    print("------------Task 4.2------------")
    print()

    lecturers_average_score_calculation([lecturer_F, lecturer_L], 'Python')
    lecturers_average_score_calculation([lecturer_F, lecturer_L], 'C#')
