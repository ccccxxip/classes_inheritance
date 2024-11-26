class Bachelor:

    def __init__(self, first_name, last_name, group, average_mark):
        self.last_name = last_name
        self.first_name = first_name
        self.group = group
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark == 5:
            return 10000
        elif self.average_mark > 3:
            return 5000
        else:
            return 0

class Undergraduate(Bachelor):

    def get_scholarship(self):
        if self.average_mark == 5:
            return 15000
        elif self.average_mark > 3:
            return 7500
        else:
            return 0

students = [
    Bachelor("Иван", "Иванов", "123", 4.4),
    Bachelor("Петр", "Петров", "345", 3.5),
    Undergraduate("Анна", "Петрова", "765", 5),
    Undergraduate("Мария", "Кузьмина", "269", 3.2)
]

for student in students:
    scholarship = student.get_scholarship()
    print(f"Студент - {student.first_name} {student.last_name}, Стипендия = {scholarship}")