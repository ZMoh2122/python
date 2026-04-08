# # Input the student's age
# age = int(input("Enter the student's age: "))

# # Determine the year group using logical operators
# if age < 4:
#     print("Too young for school in the UK.")
# elif age >= 4 and age <= 5:
#     print("Reception (Early Years Foundation Stage).")
# elif age >= 6 and age <= 10:
#     print("Year", age - 5, "(Primary School).")
# elif age >= 11 and age <= 16:
#     print("Year", age - 5, "(Secondary School).")
# elif age >= 17 and age <= 18:
#     print("Year", age - 5, "(Sixth Form/College).")
# elif age > 18:
#     print("Likely not in school anymore (Further Education or beyond).")
# else:
#     print("Invalid input. Age must be a positive number.")



# # Input the student's age and student status
# age = int(input("Enter the student's age: "))
# is_student = input("Is the person a student? (yes/no): ").lower()

# # Determine if the person qualifies for a discount using the 'or' logical operator
# if age <= 18 or is_student == 'yes':
#     print("You qualify for a discount!")
# else:
#     print("Sorry, you don't qualify for a discount.")



# Input the person's age
age = int(input("Enter the person's age: "))

# Check if the person is not allowed to enter the restricted area
if age != 18:
    print("Sorry, you are not allowed to enter the restricted area.")
else:
    print("You are allowed to enter the restricted area.")
