import employee
import task
import assignment
import reports

while True:
    print("\n========================================")
    print("             ADMIN PANEL")
    print("========================================")
    print("1. Employee Management")
    print("2. Task Management")
    print("3. Assignment Management")
    print("4. Reports & Analytics")
    print("5. Exit")
    print("========================================")

    
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            print("\n----- EMPLOYEE MANAGEMENT -----")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Search Employee")
            print("5. Delete Employee")
            print("6. Back to Admin Panel")

            emp_choice = input("Enter your choice: ")

            if emp_choice == "1":
                employee.add_emp()

            elif emp_choice == "2":
                employee.view_employees()

            elif emp_choice == "3":
                employee.update_employee()

            elif emp_choice == "4":
                employee.search_employee()

            elif emp_choice == "5":
                employee.delete_employee()

            elif emp_choice == "6":
                break

            else:
                print("Invalid choice! Please select 1 to 6.")

    elif choice == "2":
        while True:
            print("\n----- TASK MANAGEMENT -----")
            print("1. Create Task")
            print("2. View All Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Search Task")
            print("6. Filter Tasks by Status")
            print("7. Filter Tasks by Priority")
            print("8. View Overdue Tasks")
            print("9. Back to Admin Panel")

            task_choice = input("Enter your choice: ")

            if task_choice == "1":
                task.create_task()

            elif task_choice == "2":
                task.view_task()

            elif task_choice == "3":
                task.update_task()

            elif task_choice == "4":
                task.delete_task()

            elif task_choice == "5":
                task.search_task()
                
            elif task_choice == "6":
                task.filter_tasks_by_status()

            elif task_choice == "7":
                task.filter_tasks_by_priority()

            elif task_choice == "8":
                task.view_overdue_tasks()

            elif task_choice == "9":
                break

            else:
                print("Invalid choice! Please select 1 to 9.")

    elif choice == "3":
        while True:
            print("\n----- ASSIGNMENT MANAGEMENT -----")
            print("1. Assign Task")
            print("2. View Task Assignments")
            print("3. View Tasks by Employee")
            print("4. Reassign Task")
            print("5. Remove Assignment")
            print("6. Back to Admin Panel")

            assign_choice = input("Enter your choice: ")

            if assign_choice == "1":
                assignment.assign_task()

            elif assign_choice == "2":
                assignment.view_assignments()

            elif assign_choice == "3":
                assignment.view_tasks_by_employee()

            elif assign_choice == "4":
                assignment.reassign_task()

            elif assign_choice == "5":
                assignment.remove_assignment()

            elif assign_choice == "6":
                break

            else:
                print("Invalid choice! Please select 1 to 6.")

    elif choice == "4":
        reports.view_reports()

    elif choice == "5":
        print("Exiting Admin Panel. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number from 1 to 5.")
