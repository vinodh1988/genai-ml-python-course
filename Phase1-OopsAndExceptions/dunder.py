class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    
    def __str__(self): #Dunder method to return a string representation of the object
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Salary: ${self.salary:,.2f})"
    

# Create a list of employees
employees = [
    Employee("Alice Johnson", 101, "Engineering", 95000),
    Employee("Bob Smith", 102, "Marketing", 75000),
    Employee("Carol Williams", 103, "Sales", 80000),
    Employee("David Brown", 104, "HR", 70000),
]

# Print employees using __str__
for employee in employees:
    print(employee)