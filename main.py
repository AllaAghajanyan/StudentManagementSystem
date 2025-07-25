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

