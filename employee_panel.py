import employee, task
import comments

employee_id = int(input("Enter your Employee ID: "))

while True:
    print("\n========================================")
    print("            EMPLOYEE PANEL")
    print("========================================")
    print("1. View My Profile")
    print("2. View My Tasks")
    print("3. Update Task Status")
    print("4. Add Comment")
    print("5. View Completed Tasks")
    print("6. Logout")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee.view_employees_id(employee_id)

    elif choice == "2":
        task.view_my_tasks_id(employee_id)

    elif choice == "3":
        update_task_status_id(employee_id)

    elif choice == "4":
        comments.add_comment(employee_id)

    elif choice == "5":
        task.view_completed_tasks(employee_id)

    elif choice == "6":
        print("Logging out. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")
