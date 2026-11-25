# Full Name: De Vera, John Angelo
# Section: IV-BSIT C
# Activity: P1
# Date: 2026-11-15

def enter_grades():
    grades = []
    while True:
        try:
            count = int(input("How many grades will you enter? "))
            if count <= 0:
                print("Enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")
    for number in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {number} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be from 0 to 100.")
            except ValueError:
                print("Invalid input. Enter a numeric grade.")
    return grades

def compute_average(grades):
    return sum(grades) / len(grades) if grades else 0

def get_highest(grades):
    return max(grades) if grades else None

def get_lowest(grades):
    return min(grades) if grades else None

def get_status(grades, passing_mark=75):
    return "PASSED" if grades and compute_average(grades) >= passing_mark else "FAILED"

def show_results(grades):
    if not grades:
        print("No grades entered yet.")
        return
    print("\n--- STUDENT GRADE RESULTS ---")
    print(f"Average: {compute_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest: {get_lowest(grades):.2f}")
    print(f"Status: {get_status(grades)}")

def main():
    student_grades = []
    print("STUDENT GRADE CALCULATOR")
    print("Name: De Vera, John Angelo | Section: IV-BSIT C")
    while True:
        print("\n1. Enter grades\n2. View results\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            student_grades = enter_grades()
            print("Grades saved.")
        elif choice == "2":
            show_results(student_grades)
        elif choice == "3":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid menu choice. Select 1, 2, or 3.")

if __name__ == "__main__":
    main()

# A local variable exists only inside the function where it is created.
# For example, grades inside enter_grades is local to that function.
# The student_grades variable in main is also local to main.
# A global variable is created outside functions and is accessible throughout the module.
# This program avoids global variables by passing grades through function parameters.
