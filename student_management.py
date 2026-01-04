students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully")

def view_students():
    if not students:
        print("No records found")
    for roll, details in students.items():
        print(f"Roll: {roll}, Name: {details['name']}, Marks: {details['marks']}")

def update_student():
    roll = input("Enter roll number to update: ")
    if roll in students:
        marks = float(input("Enter new marks: "))
        students[roll]["marks"] = marks
        print("Record updated")
    else:
        print("Student not found")

def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Record deleted")
    else:
        print("Student not found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
