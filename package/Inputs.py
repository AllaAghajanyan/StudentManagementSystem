from package import Validations

def ask_input_method():
    while True:
        response = input("Do you want to enter student data manually? (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            return "manual"
        elif response in ["no", "n"]:
            return "file"
        else:
            print("Please answer with 'yes' or 'no'.")

def data_input():
    name = input("Enter student's first name: ").title().strip()
    surname = input("Enter student`s last name: ").title().strip()
    age = Validations.get_valid_age("Enter student's age: ")
    currentYearGrade = Validations.valid_float("Enter student's current year grade: ")
    lastYearGrade = Validations.valid_float("Enter student's last year grade: ")
    averageGrade = (currentYearGrade + lastYearGrade) / 2
    return name, surname, age, averageGrade



def open_file(file_path):
    uploaded_students = []
    emails_DB = set()

    try:
        with open(file_path, "r") as file:
            for line in file:
                student_info = line.strip().split(",")
                if len(student_info) != 5:
                    print("Invalid data format. Skipping line:", line.strip())
                    continue

                name = student_info[0].strip().title()
                surname = student_info[1].strip().title()

                try:
                    age = int(student_info[2])
                    lastYearGrade = float(student_info[3])
                    currentYearGrade = float(student_info[4])
                except ValueError:
                    print(f"Invalid numeric data. Skipping line: {line.strip()}")
                    continue

                averageGrade = (lastYearGrade + currentYearGrade) / 2
                email = f"{name.lower()}.{surname.lower()}@myschool.armstqb"

                Validations.email_uniqueness(email, emails_DB)
                emails_DB.add(email)

                category = "Primary School student" if age < 18 else "College student"
                result = "Passed" if averageGrade >= 50 else "Failed"

                student = {
                    "full_name": f"{name} {surname}",
                    "age": age,
                    "email": email,
                    "average": averageGrade,
                    "category": category,
                    "result": result
                }

                uploaded_students.append(student)

        return uploaded_students

    except FileNotFoundError:
        print("File not found. Please check the path.")



