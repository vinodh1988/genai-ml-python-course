import json

# Read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Access the students list
students = data['students']

# Example: Print all students
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}, GPA: {student['gpa']}")

# Example: Filter students with grade 'A'
grade_a_students = [s for s in students if s['grade'] == 'A']
print(f"\nStudents with grade A: {len(grade_a_students)}")

# Example: Find student by ID
def find_student_by_id(student_id):
    for student in students:
        if student['id'] == student_id:
            return student
    return None

student = find_student_by_id(5)
print(f"\nStudent with ID 5: {student}")