
student = {}

def add_student():
    name = input("Enter the name of student: ")
    grade = input("Enter the grade of student: ")
    attendance = input("Enter the attendance of student: ")
    
    student[name] = {"grade": grade, "attendance": attendance}

def update_student():
    name = input("Name of student to be updated: ")
    
    if name in student:
        grade = input("Enter the new grade: ")
        attendance = input("Enter the new attendance: ")

        student[name] = {"grade": grade, "attendance": attendance}
    else:
        print("Student not found.")

def remove_student():
    name = input("Name of student to be removed: ")
    
    if name in student:
        del student[name]
    else:
        print("Student not found.")

def display_students():
    if not student:
        print("No student records available.")
    else:
        print("\nStudent Records:")
        for name, details in student.items():
            print(f"{name}: Grade - {details['grade']}, Attendance - {details['attendance']}%")

while True:
    print("\nStudent Records Manager:")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Remove Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
