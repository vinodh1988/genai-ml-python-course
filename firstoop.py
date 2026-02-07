class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name  # Public member
        self.employee_id = employee_id  # Public member
        self.__salary = salary  # Private member (name mangling)
    
    def get_salary(self):
        """Public method to  access private salary"""
        return self.__salary
    
    def set_salary(self, salary):
        """Public method to modify private salary"""
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive")
    
    def display_info(self):
        """Display employee information"""
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: ${self.__salary}")


# Create 3 employee objects
emp1 = Employee("Alice", 50000, 101)
emp2 = Employee("Bob", 60000, 102)
emp3 = Employee("Charlie", 55000, 103)

# Access public members
print("--- Public Members Access ---")
print(f"Employee 1: {emp1.name}, ID: {emp1.employee_id}")
print(f"Employee 2: {emp2.name}, ID: {emp2.employee_id}")
print(f"Employee 3: {emp3.name}, ID: {emp3.employee_id}")

# Access private members through public methods
print("\n--- Private Members Access (via methods) ---")
emp1.display_info()  
emp2.display_info()
emp3.display_info()

# Modify private members through public methods
print("\n--- Modify Private Members ---")
emp1.set_salary(55000)
emp1.display_info()

# Attempting to access private member directly will raise AttributeError
#print(emp1.__salary)  # This will cause an error