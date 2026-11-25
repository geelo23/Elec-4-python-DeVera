# Full Name: De Vera, John Angelo
# Section: IV-BSIT C
# Activity: P4
# Date: 2026-11-15

def divide_numbers():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        result = first / second
    except ValueError:
        print("Invalid number. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Division operation finished.")

def open_text_file():
    filename = input("Enter file name: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print("You do not have permission to read this file.")
    else:
        print("\n--- FILE CONTENTS ---")
        print(content if content else "(The file is empty.)")
    finally:
        print("File operation finished.")

def main():
    print("SAFE MENU PROGRAM")
    print("Name: De Vera, John Angelo | Section: IV-BSIT C")
    while True:
        print("\n1. Divide two numbers\n2. Open a text file\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_text_file()
        elif choice == "3":
            print("Program closed.")
            break
        else:
            print("Invalid menu selection. Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
