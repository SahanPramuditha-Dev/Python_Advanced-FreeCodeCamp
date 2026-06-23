students = {}

while True:
    print("\n===== STUDENT GRADE TRACKER =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Sort by Marks (High → Low)")
    print("6. Sort by Name (A → Z)")
    print("7. Update Student Name")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists.")
        else:
            marks = int(input("Enter marks: "))
            students[name] = marks
            print("Student added successfully.")

    # 2. View All
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\nStudent List:")
            for name, marks in students.items():
                print(name, ":", marks)

    # 3. Update Marks
    elif choice == "3":
        name = input("Enter student name to update marks: ")

        if name in students:
            students[name] = int(input("Enter new marks: "))
            print("Marks updated.")
        else:
            print("Student not found.")

    # 4. Delete Student
    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    # 5. Sort by Marks (NO LAMBDA VERSION)
    elif choice == "5":
        if not students:
            print("No students found.")
        else:
            print("\nSorted by Marks (High → Low):")

            for name in sorted(students, key=students.get, reverse=True):
                print(name, ":", students[name])

    # 6. Sort by Name (Simplified)
    elif choice == "6":
        if not students:
            print("No students found.")
        else:
            print("\nSorted by Name (A → Z):")

            for name in sorted(students):
                print(name, ":", students[name])

    # 7. Update Name
    elif choice == "7":
        old_name = input("Enter current student name: ")

        if old_name in students:
            new_name = input("Enter new name: ")

            if new_name in students:
                print("New name already exists.")
            else:
                students[new_name] = students.pop(old_name)
                print("Student name updated.")
        else:
            print("Student not found.")

    # 8. Exit
    elif choice == "8":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")