import admin
import employee_panel

while True:
    print("\n========================================")
    print("      EMPLOYEE TASK TRACKING SYSTEM")
    print("========================================")
    print("1. Admin Panel")
    print("2. Employee Panel")
    print("3. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        admin.admin_menu()

    elif choice == "2":
        employee_panel.employee_menu()

    elif choice == "3":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice!")