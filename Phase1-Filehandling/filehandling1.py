import os

def write_student_data():
    filename = "students.txt"
    
    try:
        # Check if file exists and is empty
      
        file_is_empty = not os.path.exists(filename) or os.path.getsize(filename) == 0
        
        # Open file in append mode, create if doesn't exist
        with open(filename, 'a') as file:
            # Add header if file is empty
            if file_is_empty:
                file.write(f"{'SNO':<10}{'Name':<20}{'City':<15}\n")
                file.write("-" * 45 + "\n")
            
            while True:
                try:
                    sno = int(input("Enter Student Number (negative to exit): "))
                    
                    if sno < 0:
                        print("Exiting...")
                        break
                    
                    name = input("Enter Student Name: ").strip()
                    if not name:
                        print("Name cannot be empty. Try again.")
                        continue
                    
                    city = input("Enter City: ").strip()
                    if not city:
                        print("City cannot be empty. Try again.")
                        continue
                    
                    # Write formatted data to file
                    file.write(f"{sno:<10}{name:<20}{city:<15}\n")
                    print("Record added successfully!\n")
                
                except ValueError:
                    print("Invalid input! Please enter a valid number for SNO.\n")
                except Exception as e:
                    print(f"An error occurred: {e}\n")
        
        print(f"Data saved to {filename}")
    
    except IOError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    write_student_data()