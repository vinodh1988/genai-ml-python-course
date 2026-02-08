import csv

# Create a list of 10 employees
employees = [
    {"id": 1, "name": "John Smith", "position": "Manager", "salary": 75000},
    {"id": 2, "name": "Jane Doe", "position": "Developer", "salary": 65000},
    {"id": 3, "name": "Bob Johnson", "position": "Designer", "salary": 60000},
    {"id": 4, "name": "Alice Brown", "position": "Developer", "salary": 65000},
    {"id": 5, "name": "Charlie Wilson", "position": "QA Engineer", "salary": 55000},
    {"id": 6, "name": "Diana Martinez", "position": "Product Manager", "salary": 70000},
    {"id": 7, "name": "Eve Taylor", "position": "Developer", "salary": 65000},
    {"id": 8, "name": "Frank Anderson", "position": "DevOps", "salary": 68000},
    {"id": 9, "name": "Grace Lee", "position": "Data Analyst", "salary": 62000},
    {"id": 10, "name": "Henry Clark", "position": "Support", "salary": 50000},
]

# Write to CSV file
with open("writeemp.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "position", "salary"])
    writer.writeheader()
    writer.writerows(employees)

print("Data written to writeemp.csv")