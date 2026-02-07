try:
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    print(f"Hello, {name}! You are {age} years old.")
except ValueError as e:
    print("Invalid input. Please enter a valid age.")
    print(f"Error details: {e}")
else:
    print("Input was successful.")  
finally:
    print("Thank you for using the program.")