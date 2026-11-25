# Full Name: De Vera, John Angelo
# Section: IV-BSIT C
# Activity: P2 main
# Date: 2026-11-15

import datetime
import student_utils
from student_utils import calculate_average, determine_status

def read_grades():
    grades = []
    while True:
        try:
            count = int(input("How many grades? "))
            if count > 0:
                break
            print("Enter a number greater than zero.")
        except ValueError:
            print("Enter a whole number.")
    for i in range(count):
        while True:
            try:
                grade = float(input(f"Grade {i + 1} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be from 0 to 100.")
            except ValueError:
                print("Enter a valid number.")
    return grades

def main():
    print("STUDENT UTILITY REPORT")
    print("Name: De Vera, John Angelo | Section: IV-BSIT C")
    grades = read_grades()
    print("\nReport generated:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest(grades):.2f}")
    print(f"Lowest: {student_utils.get_lowest(grades):.2f}")
    print("Status:", determine_status(grades))

if __name__ == "__main__":
    main()
