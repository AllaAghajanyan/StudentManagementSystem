class Student:
    all_students = []

    def __init__(self, name, surname, age, last_year_grade, current_year_grade, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.last_year_grade = last_year_grade
        self.current_year_grade = current_year_grade
        self.email = email

        Student.all_students.append(self)

    @property
    def student_category(self):
        if self.age < 18:
            return "Primary School student"
        else:
            return "College student"


    @property
    def average_grade(self):
        average_grade = (self.last_year_grade + self.current_year_grade) / 2
        return average_grade

    @property
    def result(self):
        if self.average_grade < 50:
            return "Failed"
        else:
            return "Passed"


    def each_student(self):
        return {
            "full_name": f"{self.name} {self.surname}",
            "age": self.age,
            "email": self.email,
            "average_grade": self.average_grade,
            "category": self.student_category,
            "result": self.result
        }

    @classmethod
    def show_all_students(cls):
        for student in cls.all_students:
            print(student.each_student())
