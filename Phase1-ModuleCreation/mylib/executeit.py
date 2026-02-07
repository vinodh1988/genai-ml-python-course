import filemod
from filemod import sayHi, employees

filemod.sayHi()
for emp in filemod.employees:
    print(f"{emp['name']} is a {emp['position']} earning ${emp['salary']}.")

sayHi()
for emp in employees:
    print(f"{emp['name']} is a {emp['position']} earning ${emp['salary']}.")