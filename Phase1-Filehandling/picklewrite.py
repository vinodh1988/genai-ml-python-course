import pickle

# Create 5 employees in a dictionary
employees = {
    1: {"name": "Alice Johnson", "position": "Software Engineer", "salary": 95000},
    2: {"name": "Bob Smith", "position": "Product Manager", "salary": 105000},
    3: {"name": "Carol Davis", "position": "Data Scientist", "salary": 100000},
    4: {"name": "David Wilson", "position": "DevOps Engineer", "salary": 98000},
    5: {"name": "Eve Martinez", "position": "UX Designer", "salary": 92000}
}

# Write to pickle file
with open('picklewrite.pkl', 'wb') as file:
    pickle.dump(employees, file)

print("Employees written to pickle file successfully!")