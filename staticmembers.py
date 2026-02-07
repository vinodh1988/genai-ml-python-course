class MyClass:
    # Static variable - shared across all instances
    static_var = "I'm static"
    
    def __init__(self, instance_var):
        # Instance variable - unique to each instance
        self.instance_var = instance_var
    
    def instance_method(self):
        # Can access both instance and static variables
        return f"Instance: {self.instance_var}, Static: {MyClass.static_var}"
    
    @staticmethod
    def static_method(x, y):
        # No access to self or cls
        return x + y
    
    @classmethod
    def class_method(cls):
        # Receives class as first argument
        return f"Class variable: {cls.static_var}"


# Demonstration
obj1 = MyClass("obj1_value")
obj2 = MyClass("obj2_value")

print(obj1.instance_method())  # Instance-specific
print(obj2.instance_method())  # Different instance_var, same static_var

print(MyClass.static_method(5, 3))  # Call static method
print(MyClass.class_method())  # Call class method

# Modify static variable
MyClass.static_var = "Updated static"
print(obj1.instance_method())  # Both instances see the change

