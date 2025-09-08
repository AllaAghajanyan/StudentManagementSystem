<<<<<<< Updated upstream
def get_valid_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def valid_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid grade.")

def get_valid_age(prompt):
    while True:
        age = get_valid_int(prompt)
        if 6 <= age <= 80:
            return age
        else:
            print("Invalid age. Please enter an age between 6 and 80.")

def data_input():
    full_name = input("Enter student's full name: ")
    full_name = " ".join(part.capitalize() for part in full_name.strip().split())
    age = get_valid_age("Enter student's age: ")
    currentYearGrade = valid_float("Enter student's current year grade: ")
    lastYearGrade = valid_float("Enter student's last year grade: ")
    averageGrade = (currentYearGrade + lastYearGrade) / 2
    return full_name, age, averageGrade

student_num = get_valid_int("How many students' data are you going to enter? ")
count = 0
student_data = []

emails_DB = set()

while count < student_num:
    full_name, age, averageGrade = data_input()

    name_parts = full_name.split()
    if len(name_parts) >= 2:
        name = name_parts[0]
        surname = name_parts[1]
        email = f"{name.lower()}.{surname.lower()}@myschool.armstqb"
    else:
        name = name_parts[0]
        email = f"{name.lower()}@myschool.armstqb"

=======
from package import Validations
from package import Inputs
from package import Prints
from package.Classes import Student

input_method = Inputs.ask_input_method()
emails_DB = set()
students_data = []

if input_method == "manual":
    student_num = Validations.get_valid_int("How many students' data are you going to enter? ")
    count = 0
    while count < student_num:
        students_data.append(Inputs.data_input())
        count += 1

        if count < student_num:
            more = input("Do you want to enter another student? (yes/no): ").strip().lower()
            if more in ["no", "n"]:
                break

else:
    file_path = input("Enter the path to your student data file: ").strip()
    students_data = Inputs.open_file(file_path)

for name, surname, age, current_year_grade, last_year_grade in students_data:
    email = f"{name.lower()}.{surname.lower()}@myschool.armstqb"
    email = Validations.email_uniqueness(email, emails_DB)
    emails_DB.add(email)

    Student(
        name=name,
        surname=surname,
        age=age,
        current_year_grade=current_year_grade,
        last_year_grade=last_year_grade,
        email=email
    )

if Student.all_students:
    students_dict_list = [s.each_student() for s in Student.all_students]

    print("The data has been successfully entered.\n")
    print("Summary of all students:")
    Prints.print_student_summary(students_dict_list)

    save_file = input("Do you want to save your data file? (yes/no): ").strip().lower()
    if save_file in ["yes", "y"]:
        Prints.save_to_file(students_dict_list)

    print("\nAll operations are complete. Thank you for using the Student Data Program!")
else:
    print("No student data was entered.")
>>>>>>> Stashed changes

    while email in emails_DB:
        print(f"""Dear user, our system automatically generates email addresses for all students
        However, the email '{email}' is already used.""")

        while True:
            email = input("Please enter a different email address (must end with @myschool.armstqb): ").strip()

            if not email:
                print("Email cannot be empty. Please try again.")
            elif not email.endswith("@myschool.armstqb"):
                print("Invalid format. Must end with '@myschool.armstqb'. Try again.")
            elif email in emails_DB:
                print(f"The email '{email}' is already used. Please enter a unique one.")
            else:
                break

    emails_DB.add(email)

    if age < 18:
        category = "Primary School student"
    else:
        category = "College student"

    if averageGrade >= 50:
        result = "Passed"
        message = f"{full_name}, {age}, You are a {category}. Your average grade is {averageGrade}. Congratulations, you passed!"
    else:
        result = "Failed"
        message = f"{full_name}, {age}, You are a {category}. Your average grade is {averageGrade}. Unfortunately, you failed."

    print(message)


    student_data.append({
        "name": full_name,
        "age": age,
        "average": averageGrade,
        "category": category,
        "result": result,
        "email": email
    })
    count = count + 1


    if count < student_num:
        while True:
            more = input("Do you want to enter another student? (yes/no): ").strip().lower()
            if more in ["yes", "y"]:
                break
            elif more in ["no", "n"]:
                count = student_num
                break
            else:
                print("Please answer with 'yes' or 'no'.")

print("The data has been successfully entered.")
print("Summary of all students:")

for i, student in enumerate(student_data, start=1):
    print(f"{i}. Name: {student['name']}, Age: {student['age']}, Email: {student['email']} Average score: {student['average']}, "
          f"{student['category']} — {student['result']}")

