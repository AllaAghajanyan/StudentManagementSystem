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

def email_uniqueness(email, emails_DB):
    while email in emails_DB:
        print(f"""Dear user, our system automatically generates email addresses
for all students. However, the email '{email}' is already in use.""")
        print()
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
    return email