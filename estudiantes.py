# student_management.py

# Preload the list of 5 students
def preload_students():
    # List of students, each represented as a dictionary
    students = [
        {"name": "Alice", "age": 15, "grade": 10, "average": 9.2, "year_of_entry": 2020},
        {"name": "Bob", "age": 17, "grade": 12, "average": 8.5, "year_of_entry": 2019},
        {"name": "Charlie", "age": 14, "grade": 9, "average": 7.8, "year_of_entry": 2021},
        {"name": "David", "age": 16, "grade": 11, "average": 6.9, "year_of_entry": 2020},
        {"name": "Eve", "age": 18, "grade": 12, "average": 9.5, "year_of_entry": 2018}
    ]
    return students

# Function to register a new student
def register_student(students, name, age, grade, average, year_of_entry):
    # Validate age (between 5 and 18) and average (between 0 and 10)
    if age < 5 or age > 18:
        print("Error: Age must be between 5 and 18.")
        return
    if average < 0 or average > 10:
        print("Error: Average must be between 0 and 10.")
        return
    
    # Create a new student dictionary and append to the students list
    student = {"name": name, "age": age, "grade": grade, "average": average, "year_of_entry": year_of_entry}
    students.append(student)
    print(f"Student {name} registered successfully.")

# Function to search for students by name or grade
def search_student(students, query):
    # List to store matching students
    results = []
    for student in students:
        # Check if query matches either the name or grade
        if query.lower() in student["name"].lower() or query.lower() in str(student["grade"]):
            results.append(student)
    return results

# Function to update a student's grade or average
def update_student(students, student_name, new_grade=None, new_average=None):
    for student in students:
        if student["name"].lower() == student_name.lower():
            # Update grade if provided and valid
            if new_grade is not None and 1 <= new_grade <= 12:
                student["grade"] = new_grade
            # Update average if provided and valid
            if new_average is not None and 0 <= new_average <= 10:
                student["average"] = new_average
            print(f"Student {student_name} updated successfully.")
            return
    print(f"Student {student_name} not found.")

# Function to delete a graduate
def delete_graduate(students, student_name):
    for student in students:
        if student["name"].lower() == student_name.lower():
            confirm = input(f"Are you sure you want to delete {student_name}? (yes/no): ")
            if confirm.lower() == 'yes':
                students.remove(student)
                print(f"Student {student_name} deleted successfully.")
                return
            else:
                print("Deletion canceled.")
                return
    print(f"Student {student_name} not found.")

# Function to generate reports
def generate_reports(students):
    # Report for average grade by grade level
    grade_averages = {}
    for student in students:
        if student["grade"] not in grade_averages:
            grade_averages[student["grade"]] = []
        grade_averages[student["grade"]].append(student["average"])
    
    # Print average by grade
    print("\nAverage grade by grade level:")
    for grade, averages in grade_averages.items():
        print(f"Grade {grade}: {sum(averages)/len(averages):.2f}")

    # Report for outstanding students (average >= 9)
    print("\nOutstanding students (average >= 9):")
    for student in students:
        if student["average"] >= 9:
            print(f"Student: {student['name']}, Average: {student['average']}")

# Main interactive menu function
def menu():
    # Preload the list of students
    students = preload_students()

    while True:
        # Display the menu
        print("\n--- Student Management System ---")
        print("1. Register Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Graduate")
        print("5. Generate Reports")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for student details and register the student
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = int(input("Enter student grade (1-12): "))
            average = float(input("Enter student average (0-10): "))
            year_of_entry = int(input("Enter year of entry: "))
            register_student(students, name, age, grade, average, year_of_entry)

        elif choice == '2':
            # Prompt for search query and display matching students
            query = input("Enter student name or grade to search: ")
            results = search_student(students, query)
            if results:
                for result in results:
                    print(f"Student: {result['name']}, Age: {result['age']}, Grade: {result['grade']}, Average: {result['average']}, Year of Entry: {result['year_of_entry']}")
            else:
                print("No students found.")

        elif choice == '3':
            # Prompt for student name to update and new values for grade or average
            student_name = input("Enter student name to update: ")
            new_grade = input("Enter new grade (1-12, or leave blank to skip): ")
            new_average = input("Enter new average (0-10, or leave blank to skip): ")

            new_grade = int(new_grade) if new_grade else None
            new_average = float(new_average) if new_average else None
            update_student(students, student_name, new_grade, new_average)

        elif choice == '4':
            # Prompt for student name to delete
            student_name = input("Enter student name to delete: ")
            delete_graduate(students, student_name)

        elif choice == '5':
            # Generate reports
            generate_reports(students)

        elif choice == '6':
            # Exit the system
            print("Exiting the student management system.")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    menu()
