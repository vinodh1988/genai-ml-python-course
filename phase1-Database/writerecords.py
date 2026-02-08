import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="genai"
)

cursor = conn.cursor()

try:
    # Fetch all records from person table
    select_query = "SELECT sno, name, city FROM person"
    cursor.execute(select_query)
    records = cursor.fetchall()
    
    if records:
        # Print formatted table header
        print("\n" + "-" * 50)
        print(f"{'SNO':<10} {'NAME':<20} {'CITY':<20}")
        print("-" * 50)
        
        # Print each record
        for record in records:
            sno, name, city = record
            print(f"{sno:<10} {name:<20} {city:<20}")
        
        print("-" * 50)
        print(f"Total records: {len(records)}\n")
    else:
        print("No records found in the person table.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()