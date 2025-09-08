
def print_student_summary(student_data):
    for i, student in enumerate(student_data, start=1):
            print(f"""{i}.
Name       : {student['full_name']}
Age        : {student['age']}
Email      : {student['email']}
Average    : {student['average']}
Category   : {student['category']}
Result     : {student['result']}
""")

def save_to_file(student_data):
    with open("StudentsReport.txt", "w") as file:
        for i, student in enumerate(student_data, start=1):
                file.write(f"""{i}.
    Name       : {student['full_name']}
    Age        : {student['age']}
    Email      : {student['email']}
    Average    : {student['average']}
    Category   : {student['category']}
    Result     : {student['result']}

    """)