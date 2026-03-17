age_input = input("please enter your age: ")
age = int(age_input)
if age < 0:
    print("Age cannot be negative.")
else:
    matinee_input = input("Is it a matinee showing? (yes/no): ").strip().lower()
is_matinee = True if matinee_input == "yes" else False
if age < 13:
    if is_matinee:
        print("Your ticket price is 6.00.")
    else:
        print("Your ticket price is 8.00.")
elif 13<= age <17:
    if is_matinee:
        print("Your ticket price is 7.00.")
    else:
        print("Your ticket price is 10.00.")
elif 17 <= age <= 64:
    if is_matinee:
        print("Your ticket price is 8.00.")
    else:
        print("Your ticket price is 13.00.")
else:
    if is_matinee:
        print("Your ticket price is 6.00.")
    else:
        print("Your ticket price is 7.00.")
        
        print("your ticket price is: ${price:.2f}")