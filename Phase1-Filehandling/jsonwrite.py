import json

# Create a list of 10 student dictionaries
students = [
    {"id": 1, "name": "Alice Johnson", "age": 20, "gpa": 3.8},
    {"id": 2, "name": "Bob Smith", "age": 19, "gpa": 3.5},
    {"id": 3, "name": "Charlie Brown", "age": 21, "gpa": 3.9},
    {"id": 4, "name": "Diana Prince", "age": 20, "gpa": 3.7},
    {"id": 5, "name": "Ethan Hunt", "age": 22, "gpa": 3.6},
    {"id": 6, "name": "Fiona Green", "age": 19, "gpa": 3.8},
    {"id": 7, "name": "George Miller", "age": 20, "gpa": 3.4},
    {"id": 8, "name": "Hannah White", "age": 21, "gpa": 3.9},
    {"id": 9, "name": "Isaac Newton", "age": 20, "gpa": 3.7},
    {"id": 10, "name": "Julia Roberts", "age": 19, "gpa": 3.5}
]

# Write to JSON file
with open('studentwrite.json', 'w') as f:
    json.dump(students, f, indent=2)

print("Students written to studentwrite.json")