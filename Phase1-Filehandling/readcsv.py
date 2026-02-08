import csv

# Read the CSV file
with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)