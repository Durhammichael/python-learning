

errors = []
student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

if len(student_id) != 8:
    errors.append("Student ID must be exactly 8 characters.")
else:
    if not student_id[0].isalpha():
        errors.append("Student ID must start with a letter.")
    if not student_id[1:].isdigit():
        errors.append("Last 7 characters of Student ID must be digits.")
if len(name.strip()) < 2:
    errors.append("Name must be at least 2 characters and not empty.") 
age = int(age_input)
if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99.")
except ValueError:
errors.append("Age must be a valid integer.")
valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append("Major must be one of: CS, IT, CE, DS.")
    