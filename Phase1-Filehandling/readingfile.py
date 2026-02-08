# Read and parse the students.txt file
with open('students.txt', 'r') as file:
    content = file.read()
    print(content)

# Or, to parse it into structured data:
with open('students.txt', 'r') as file:
    lines = file.readlines()
    
students = []
for line in lines[2:]:  # Skip header lines
    if line.strip():
        parts = line.split()
        if parts[0].isdigit():
            students.append({
                'SNO': parts[0],
                'Name': parts[1],
                'City': parts[2]
            })

for student in students:
    print(student)