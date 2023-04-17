class University:
    def __init__(self, name):
        self.faculties = []
        self.name = name

    # 1
    def create_faculty(self):
        name = input("Введіть назву факультету: ")
        for faculty in self.faculties:
            if faculty.name == name:
                print("Такий факультет вже існує!")
                return
        faculty = Faculty(name)
        self.faculties.append(faculty)
        print(f"Факультет '{faculty.name}' було успішно створено.")

    # 2
    def remove_faculty(self):
        name = input("Введіть назву факультету, який ви хочете видалити: ")
        for faculty in self.faculties:
            if faculty.name == name:
                self.faculties.remove(faculty)
                print(f"Факультет було видалено.")
                return
        print(f"Такого факультету немає.")

    # 3
    def edit_faculty(self):
        name = input("Введіть назву факультету, який ви хочете змінити: ")
        for faculty in self.faculties:
            if faculty.name == name:
                new_name = input("Введіть нову назву факультету: ")
                faculty.name = new_name
                print(f"Назву факультету було змінено на '{faculty.name}'.")
                return
        print("Такого факультету немає.")

    # 13
    def find_student_by_name(self):
        name = input("Введіть ПІБ: ")
        results = []
        for faculty in self.faculties:
            for department in faculty.departments:
                for student in department.students:
                    if name in student.name:
                        results.append(student)
        if results:
            print(f"Знайдено {len(results)} студентів з ПІБ '{name}':")
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print(f"Студента з ПІБ '{name}' не знайдено.")

    # 14
    def find_student_by_course(self):
        course = input("Введіть курс: ")
        results = []
        for faculty in self.faculties:
            for department in faculty.departments:
                for student in department.students:
                    if course in student.course:
                        results.append(student)
        if results:
            print(f"Знайдено {len(results)} студентів з курсу '{course}': ")
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print(f"Студентів з курсу '{course}' не знайдено.")

    # 15
    def find_student_by_group(self):
        group = input("Введіть групу: ")
        results = []
        for faculty in self.faculties:
            for department in faculty.departments:
                for student in department.students:
                    if group in student.group:
                        results.append(student)
        if results:
            print(f"Знайдено {len(results)} студентів з групи '{group}':")
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print(f"Студентів з групи '{group}' не знайдено.")

    # 16
    def find_teacher_by_name(self):
        name = input("Введіть ПІБ: ")
        results = []
        for faculty in self.faculties:
            for department in faculty.departments:
                for teacher in department.teachers:
                    if name in teacher.name:
                        results.append(teacher)
        if results:
            print(f"Знайдено {len(results)} викладачів з ПІБ '{name}':")
            for teacher in results:
                print(teacher.name, ", ", teacher.position)
        else:
            print(f"Викладача з ПІБ '{name}' не знайдено.")

    # 17
    def all_students_sorted_by_course(self):
        all_students = []
        for faculty in self.faculties:
            for department in faculty.departments:
                all_students.extend(department.students)
        results = sorted(all_students, key=lambda s: s.course)
        if len(results) > 0:
            print("Усі студенти, відсортовані за курсом: ")
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print("В університеті немає студентів.")


class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []

    # 4
    def create_department(self):
        name = input("Введіть назву кафедри: ")
        for department in self.departments:
            if department.name == name:
                print("Така кафедра вже існує!")
                return
        department = Department(name)
        self.departments.append(department)
        print(f"Кафедру '{department.name}' було успішно створено.")

    # 5
    def remove_department(self):
        department_name = input("Введіть назву кафедри, яку ви хочете видалити: ")
        for department in self.departments:
            if department.name == department_name:
                self.departments.remove(department)
                print(f"Кафедру було видалено.")
                return
        print("Такої кафедри немає!")

    # 6
    def edit_department(self):
        department_name = input("Введіть назву кафедри, яку ви хочете змінити: ")
        for department in self.departments:
            if department.name == department_name:
                new_name = input("Введіть нову назву кафедри: ")
                department.name = new_name
                print(f"Назву кафедри було змінено на '{department.name}'.")
                return
        print(f"Кафедру '{department_name}' не знайдено!")

    # 18
    def students_sorted_by_name(self):
        all_students = []
        for department in self.departments:
            all_students.extend(department.students)
        results = sorted(all_students, key=lambda s: s.name)
        if len(results) > 0:
            print("Студенти факультету, відсортовані за іменем: ")
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print("На факультеті немає студентів.")

    # 19
    def teachers_sorted_by_name(self):
        all_teachers = []
        for department in self.departments:
            all_teachers.extend(department.teachers)
        results = sorted(all_teachers, key=lambda t: t.name)
        if len(results) > 0:
            print("Викладачі факультету, відсортовані за іменем: ")
            for teacher in results:
                print(teacher.name, ", ", teacher.position)
        else:
            print("На факультеті немає викладачів.")


class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    # 7
    def create_student(self):
        name = input("Введіть ім'я студента: ")
        course = input("Введіть курс студента: ")
        group = input("Введіть групу студента: ")
        for student in self.students:
            if student.name == name and student.course == course and student.group == group:
                print("Такий студент уже існує!")
                return
        student = Student(name, course, group)
        self.students.append(student)
        print(f"Студента '{student.name}' успішно створено.")

    # 8
    def remove_student(self):
        name = input("Введіть ім'я студента, якого хочете видалити: ")
        course = input("Введіть курс студента: ")
        group = input("Введіть групу студента: ")
        for student in self.students:
            if student.name == name and student.course == course and student.group == group:
                self.students.remove(student)
                print("Студента було видалено.")
                return
        print("Такого студента немає!")

    # 9
    def edit_student(self):
        name = input("Введіть ім'я студента, якого хочете змінити: ")
        course = input("Введіть курс студента: ")
        group = input("Введіть групу студента: ")
        for student in self.students:
            if student.name == name and student.course == course and student.group == group:
                new_name = input("Введіть нове ім'я: ")
                new_course = input("Введіть новий курс: ")
                new_group = input("Введіть нову групу: ")
                student.name = new_name
                student.course = new_course
                student.group = new_group
                print("Студента було успішно змінено.")
                return
        print("Такого студента немає!")

    # 10
    def create_teacher(self):
        name = input("Введіть ім'я викладача: ")
        position = input("Введіть посаду викладача: ")
        for teacher in self.teachers:
            if teacher.name == name and teacher.position == position:
                print("Такий викладач уже існує!")
                return
        teacher = Teacher(name, position)
        self.teachers.append(teacher)
        print(f"Викладача {teacher.name} успішно створено.")

    # 11
    def remove_teacher(self):
        name = input("Введіть ім'я викладача, якого хочете видалити: ")
        position = input("Введіть посаду викладача: ")
        for teacher in self.teachers:
            if teacher.name == name and teacher.position == position:
                self.teachers.remove(teacher)
                print("Викладача було видалено.")
                return
        print("Такого викладача немає!")

    # 12
    def edit_teacher(self):
        name = input("Введіть ім'я викладача, якого хочете змінити: ")
        position = input("Введіть посаду викладача: ")
        for teacher in self.teachers:
            if teacher.name == name and teacher.position == position:
                new_name = input("Введіть нове ім'я: ")
                new_position = input("Введіть нову посаду: ")
                teacher.name = new_name
                teacher.position = new_position
                print("Викладача було успішно змінено.")
                return
        print("Такого викладача немає!")

    # 20
    def students_sorted_by_course(self):
        all_students = []
        for student in self.students:
            all_students.append(student)
        results = sorted(all_students, key=lambda s: s.course)
        if len(results) > 0:
            print("Студенти кафедри, відсортовані за курсом: ")
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print("На кафедрі немає студентів.")

    # 21
    def students_sorted_by_name(self):
        all_students = []
        for student in self.students:
            all_students.append(student)
        results = sorted(all_students, key=lambda s: s.name)
        if len(results) > 0:
            print("Студенти кафедри, відсортовані за іменем: ")
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print("На кафедрі немає студентів.")

    # 22
    def teachers_sorted_by_name(self):
        all_teachers = []
        for teacher in self.teachers:
            all_teachers.append(teacher)
        results = sorted(all_teachers, key=lambda t: t.name)
        if len(results) > 0:
            print("Викладачі кафедри, відсортовані за іменем: ")
            for teacher in results:
                print(teacher.name, ", ", teacher.position)
        else:
            print("На кафедрі немає викладачів.")

    # 23
    def students_by_course(self):
        course = input("Введіть курс: ")
        all_students = []
        for student in self.students:
            if student.course == course:
                all_students.append(student)
        if len(all_students) > 0:
            for student in all_students:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print("На кафедрі немає студентів із заданого курсу.")

    # 24
    def students_by_course_sorted_by_name(self):
        course = input("Введіть курс: ")
        all_students = []
        for student in self.students:
            if student.course == course:
                all_students.append(student)
        results = sorted(all_students, key=lambda s: s.name)
        if len(results) > 0:
            for student in results:
                print(student.name, ", ", student.course, ", ", student.group)
        else:
            print("На кафедрі немає студентів із заданого курсу.")


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course, group):
        super().__init__(name)
        self.course = course
        self.group = group


class Teacher(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position


def main():
    u1 = University("NaUKMA")
    while True:
        print("1. Створити факультет")
        print("2. Видалити факультет")
        print("3. Редагувати факультет")
        print("4. Створити кафедру")
        print("5. Видалити кафедру")
        print("6. Редагувати кафедру")
        print("7. Додати студента")
        print("8. Видалити студента")
        print("9. Редагувати студента")
        print("10. Додати викладача")
        print("11. Видалити викладача")
        print("12. Редагувати викладача")
        print("13. Знайти студента за ПІБ")
        print("14. Знайти студента за курсом")
        print("15. Знайти студента за групою")
        print("16. Знайти викладача за ПІБ")
        print("17. Вивести всіх студентів за курсами")
        print("18. Вивести всіх студентів факультету за алфавітом")
        print("19. Вивести всіх викладачів факультету за алфавітом")
        print("20. Вивести студентів кафедри за курсами")
        print("21. Вивести студентів кафедри за алфавітом")
        print("22. Вивести викладачів кафедри за алфавітом")
        print("23. Вивести всіх студентів кафедри заданого курсу")
        print("24. Вивести всіх студентів кафедри заданого курсу за алфавітом")
        print("Щоб закінчити роботу, напишіть 'quit' ")
        choice = input("Оберіть дію: ")

        if choice == "1":
            u1.create_faculty()

        elif choice == "2":
            u1.remove_faculty()

        elif choice == "3":
            u1.edit_faculty()

        elif choice == "4":
            name = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name:
                    faculty.create_department()

        elif choice == "5":
            name = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name:
                    faculty.remove_department()

        elif choice == "6":
            name = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name:
                    faculty.edit_department()

        elif choice == "7":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.create_student()

        elif choice == "8":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.remove_student()

        elif choice == "9":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.edit_student()

        elif choice == "10":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.create_teacher()

        elif choice == "11":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.remove_teacher()

        elif choice == "12":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.edit_teacher()

        elif choice == "13":
            u1.find_student_by_name()

        elif choice == "14":
            u1.find_student_by_course()

        elif choice == "15":
            u1.find_student_by_group()

        elif choice == "16":
            u1.find_teacher_by_name()

        elif choice == "17":
            u1.all_students_sorted_by_course()

        elif choice == "18":
            name = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name:
                    faculty.students_sorted_by_name()

        elif choice == "19":
            name = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name:
                    faculty.teachers_sorted_by_name()

        elif choice == "20":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.students_sorted_by_course()

        elif choice == "21":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.students_sorted_by_name()

        elif choice == "22":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.teachers_sorted_by_name()

        elif choice == "23":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.students_by_course()

        elif choice == "24":
            name1 = input("Введіть назву факультету: ")
            for faculty in u1.faculties:
                if faculty.name == name1:
                    name2 = input("Введіть назву кафедри: ")
                    for department in faculty.departments:
                        if department.name == name2:
                            department.students_by_course_sorted_by_name()

        elif choice.lower() == "quit":
            break

        else:
            print("Будь ласка, оберіть вашу дію або напишіть 'quit' для виходу.")
            continue


main()
