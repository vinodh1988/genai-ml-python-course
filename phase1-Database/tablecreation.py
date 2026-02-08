import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="genai"
)

cursor = conn.cursor()

# Create person table
create_table_query = """
CREATE TABLE IF NOT EXISTS person (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
)
"""

cursor.execute(create_table_query)
conn.commit()

print("Person table created successfully!")

cursor.close()
conn.close()