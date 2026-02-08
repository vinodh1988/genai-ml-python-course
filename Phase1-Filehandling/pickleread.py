import pickle

# Read from pickle file
with open('picklewrite.pkl', 'rb') as file:
    employees = pickle.load(file)

# Display the employees
for emp_id, emp_info in employees.items():
    print(f"ID: {emp_id}")
    print(f"Name: {emp_info['name']}")
    print(f"Position: {emp_info['position']}")
    print(f"Salary: ${emp_info['salary']}")
    print()