from package import Validations
from package import Inputs
from package import Prints

input_method = Inputs.ask_input_method()

student_data = []

if input_method == "manual":
    student_num = Validations.get_valid_int("How many students' data are you going to enter? ")
    count = 0
    emails_DB = set()

    while count < student_num:
        name, surname, age, averageGrade = Inputs.data_input()
        email = f"{name.lower()}.{surname.lower()}@myschool.armstqb"

        Validations.email_uniqueness(email, emails_DB)
        emails_DB.add(email)

        if age < 18:
            category = "Primary School student"
        else:
            category = "College student"

        if averageGrade >= 50:
            result = "Passed"
            message = f"{name} {surname}, {age}, You are a {category}. Your average grade is {averageGrade}. Congratulations, you passed!"
        else:
            result = "Failed"
            message = f"{name} {surname}, {age}, You are a {category}. Your average grade is {averageGrade}. Unfortunately, you failed."

        print(message)
        print()

        student_data.append({
            "full_name": " ".join([name, surname]),
            "age": age,
            "email": email,
            "average": averageGrade,
            "category": category,
            "result": result

        })

        count += 1

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

elif input_method == "file":
    file_path = input("Enter the path to your student data file: ").strip()
    try:
        student_data = Inputs.open_file(file_path)

    if not student_data:
        print("No valid student data to display.")

if student_data:
    print("The data has been successfully entered.\n")
    print("Summary of all students:")

    Prints.print_student_summary(student_data)

    save_file = input("Do you want to save your data file? (yes/no): ").strip().lower()
    if save_file in ["yes", "y"]:
        Prints.save_to_file(student_data)




