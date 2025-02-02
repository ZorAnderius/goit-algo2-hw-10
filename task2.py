from matplotlib.style.core import available


class Teacher:
    def __init__(self, first_name: str, last_name: str, age: int, email:str, subjects: set[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.subjects = subjects
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    schedule = []
    remaining_subjects = set(subjects)
    available_teachers = sorted(teachers, key=lambda t: (-len(t.subjects), t.age))

    for teacher in available_teachers:
        teachable_subjects = teacher.subjects & remaining_subjects
        if teachable_subjects:
            teacher.assigned_subjects = teachable_subjects
            schedule.append(teacher)
            remaining_subjects -= teachable_subjects

        if not remaining_subjects:
            return schedule

    return None if remaining_subjects else schedule


if __name__ == '__main__':
    # Множина предметів
    subjects =  {'Географія', 'Математика', 'Історія України', 'Фізика', 'Українська література', 'Інформатика', 'Українська мова'}
    # Створення списку викладачів
    teachers = [
        Teacher("Олена", "Іваненко", 35, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Дмитро", "Петренко", 50, "d.petrenko@example.com", {'Українська література', 'Інформатика'}),
        Teacher("Наталія", "Коваленко", 42, "n.kovalenko@example.com", {'Географія', 'Історія України'}),
        Teacher("Сергій", "Іваненко", 29, "s.ivanenko@example.com", {'Математика', 'Інформатика'}),
        Teacher("Марія", "Петренко", 45, "m.petrenko@example.com", {'Українська література', 'Українська мова'}),
        Teacher("Олександр", "Коваленко", 38, "o.kovalenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Максим", "Іваненко", 32, "m.ivanenko@example.com", {'Українська література', 'Історія України'}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
