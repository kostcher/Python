# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_short_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.patronymic[0] + '.'


class Parent(Person):
    pass


class Teacher(Person):
    def __init__(self, name, surname, patronymic, subject):
        self.teacher = Person.__init__(self, name, surname, patronymic)
        self.subject = subject


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_students(self):
        return [student.get_short_name() for student in self.students]

    def get_teachers(self):
        return [teacher.get_short_name() for teacher in self.teachers]


class Student(Person):
    def __init__(self, name, surname, patronymic, mother, father):
        self.student = Person.__init__(self, name, surname, patronymic)
        self.mother = mother
        self.father = father


class School:
    def __init__(self):
        self.classes = [];

    def add_class(self, class_name):
        self.classes.append(class_name)

    def get_class_rooms(self):
        return [class_room.name for class_room in self.classes]

    def get_student_subjects(self, searched_student):
        subjects = []

        for class_room in self.classes:
            for student in class_room.students:
                if student == searched_student:
                    for teacher in class_room.teachers:
                        subjects.append(teacher.subject)

        return subjects


mother_1 = Parent('Мать', 'Мать', 'Мать')
father_1 = Parent('Отец', 'Отец', 'Отец')
student_1 = Student('Иван', 'Иванов', 'Иванович', mother_1, father_1)
student_2 = Student('Петр', 'Петров', 'Петровнович', mother_1, father_1)


# 1. Получить полный список всех классов школы
school_1 = School()
class_1 = ClassRoom('1А')
class_2 = ClassRoom('2А')
class_3 = ClassRoom('3А')
school_1.add_class(class_1)
school_1.add_class(class_2)
school_1.add_class(class_3)

print(school_1.get_class_rooms())
print('\n')

# 2. Получить список всех учеников в указанном классе
class_1.add_student(student_1)
class_2.add_student(student_2)

print(class_1.get_students())
print('\n')

# 4. Узнать ФИО родителей указанного ученика
print(student_1.mother.get_short_name())
print(student_1.father.get_short_name())
print('\n')

# 5. Получить список всех Учителей, преподающих в указанном классе
teacher_1 = Teacher('Мария', 'Иванова_1', 'Ивановна', 'Математика')
teacher_2 = Teacher('Мария', 'Иванова_2', 'Ивановна', 'Информатика')
class_1.add_teacher(teacher_1)
class_1.add_teacher(teacher_2)

print(class_1.get_teachers())
print('\n')

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# student_1 - обьект ученика, предметы которого нужно получить
print(school_1.get_student_subjects(student_1))