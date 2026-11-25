# Full Name: De Vera, John Angelo
# Section: IV-BSIT C
# Activity: P3
# Date: 2026-11-15

students = []
student_keys = set()

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    key = name.casefold()
    if key in student_keys:
        print("This student is already in the record.")
        return
    students.append(name)
    student_keys.add(key)
    print(f"{name} added successfully.")

def remove_student():
    name = input("Enter the exact student name to remove: ").strip()
    key = name.casefold()
    for saved_name in students:
        if saved_name.casefold() == key:
            students.remove(saved_name)
            student_keys.remove(key)
            print(f"{saved_name} removed.")
            return
    print("Student not found.")

def search_student():
    query = input("Enter all or part of a name: ").strip().casefold()
    matches = [name for name in students if query in name.casefold()]
    if matches:
        print("Search results:")
        for name in sorted(matches, key=str.casefold):
            print("-", name)
    else:
        print("No matching student found.")

def display_students():
    print("\n--- STUDENT LIST ---")
    ordered = sorted(students, key=str.casefold)
    if not ordered:
        print("No students in the record.")
    for number, name in enumerate(ordered, start=1):
        print(f"{number}. {name}")
    print("Total students:", len(students))

def main():
    print("STUDENT RECORD MANAGER")
    print("Name: De Vera, John Angelo | Section: IV-BSIT C")
    while True:
        print("\n1. Add\n2. Remove\n3. Search\n4. Display all\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1": add_student()
        elif choice == "2": remove_student()
        elif choice == "3": search_student()
        elif choice == "4": display_students()
        elif choice == "5":
            print("Goodbye.")
            break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()

# A list stores the student names and keeps their insertion order.
# A set stores normalized names so the program quickly checks for duplicates.
# The set treats names with different letter cases as the same by using casefold().
# The list is used for searching, removing, sorting, and displaying the names.
