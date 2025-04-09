student={}
def add_student():
    name=input("enter the name of student:")
    grade=input("enter the grade of student:")
    attendance=input("enter the attendance of student:")
    student.update({"name":name,"grade":grade,"attendance":attendance})
    print(student)
def update_students():
    name=input("Name of student to be updated:")
    if name in student:
        grade=input("Enter the new grade")
        attendance=input("Enter the new attendance")
        student.update({"name":name,"grade":grade,"attendance":attendance})
        print(student)
def remove_students():
    name=input("Name of student to be removed:")
    if name in student:
        student.pop("name")
        student.pop("grade")
        student.pop("attendance")
        print(student)

student_records = {}
while True:
    print("\nStudent Records Manager:")
    print("1. Add Student")
    print("2. Update" )
    print("3. Remove Student")
    print("4.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_students()
    elif choice == "3":
        remove_students()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")