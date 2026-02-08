import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="genai"
)

cursor = conn.cursor()

print("Enter person records (enter negative sno to stop):\n")

while True:
    try:
        sno = int(input("Enter sno: "))
        
        if sno < 0:
            print("Stopping record entry.")
            break
        
        name = input("Enter name: ")
        city = input("Enter city: ")
        
        insert_query = "INSERT INTO person (sno, name, city) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (sno, name, city))
        conn.commit()
        
        print("Record inserted successfully!\n")
    
    except ValueError:
        print("Invalid input. Please enter valid data.\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()

print("All records inserted successfully!")

cursor.close()
conn.close()