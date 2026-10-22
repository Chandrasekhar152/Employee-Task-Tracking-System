import employee
import task
import assignment
import reports

while True:
    print("\n========================================")
    print("             ADMIN PANEL")
    print("========================================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Create Task")
    print("4. View All Tasks")
    print("5. Assign Task")
    print("6. View Reports")
    print("7. View Task Assignments")
    print("8. Delete Task")
    print("9. Exit")
    print("========================================")   


    choice = input("Enter your choice: ")   

    if choice == "1":
        print("\nAdd Employee selected")
        employee.add_emp()  

    elif choice == "2":
        print("\nView Employees selected")
        employee.view_employees()   

    elif choice == "3":
        print("\nCreate Task selected")
        task.create_task()  

    elif choice == "4":
        print("\nView All Tasks selected")
        task.view_task()    

    elif choice == "5":
        print("\nAssign Task selected")
        assignment.assign_task()    

    elif choice == "6":
        print("\nView Reports selected")
        reports.view_reports()  

    elif choice == "7":
        print("\nView Task Assignments selected")
        assignment.view_assignments()   

    elif choice == "8":
        print("\nDelete Task selected")
        task.delete_task()  

    elif choice == "9":
        print("Exiting Admin Panel. Goodbye!")
        break   

    else:
        print("Invalid choice! Please enter a number from 1 to 9.")
