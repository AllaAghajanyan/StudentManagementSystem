full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
currentYearGrade = float(input("Enter your current year grade: "))
lastYearGrade = float(input("Enter your last year grade: "))
AverageGrade = (currentYearGrade + lastYearGrade) / 2


if AverageGrade < 50 and  6 <= age <= 18:
    print(f"{full_name}, {age}, You are a Primary School student. Your average grade is {AverageGrade}. Unfortunately, you failed.")
elif AverageGrade >= 50 and 6 <= age <= 18:
    print(f"{full_name}, {age}, You are a Primary School student. Your average grade is {AverageGrade}. Congratulations, you passed." )
elif AverageGrade < 50 and  18 <= age <= 23:
    print(f"{full_name}, {age}, You are a College student. Your average grade is {AverageGrade}. Unfortunately, you failed.")
elif AverageGrade >= 50 and 18 <= age <= 23:
    print(f"{full_name}, {age}, You are a College student. Your average grade is {AverageGrade}. Congratulations, you passed.")
else:
    print ("Error")

