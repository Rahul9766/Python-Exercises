# Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def employee(name,salary=10000):
    print("emplyee Name: ",name)
    print("emplyee Salary: ",salary)


employee('Rahul',13000)
employee('Sumit')