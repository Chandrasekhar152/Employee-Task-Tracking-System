import db_connection

def add_emp():
    emp_id = int(input("Enter employee id: "))
    emp_name = input("Enter employee name: ")
    emp_email = input('Enter email: ')
    emp_role = input("Enter employee role: ")

    query = """ INSERT INTO EMPLOYEES (ID, NAME, ROLE, EMAIL, CREATED_AT) VALUES (%s, %s, %s, %s, NOW()) """
    values = (emp_id, emp_name, emp_role, emp_email)

    connection = db_connection.db_conn()    

    cursor = connection.cursor()    

    cursor.execute(query,values)
    connection.commit()
    cursor.close()
    connection.close()

def view_employees():
    connection = db_connection.db_conn()    

    cursor = connection.cursor()    
    cursor.execute('SELECT * FROM EMPLOYEES')
    employees = cursor.fetchall()   
    
    for employee in employees:
        print(employee)

    cursor.close()
    connection.close()

def update_employee():
    conn = db_connection.db_conn()
    cursor = conn.cursor()
    
    choice = input('Do you want to modify employee name by id: (yes/no)').lower()
    
    if choice=='yes':
        query = 'UPDATE employees SET NAME =  %s WHERE id = %s'
        emp_id = int(input('Enter emp id: '))
        name = input('Enter the modied name: ')
        value = (name, emp_id)

        cursor.execute(query, value)
        conn.commit()

        cursor.close()
        conn.close()

    else:
        print('Thank no updates')

def search_employee():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    
    print("\n========================================")
    print("          SEARCH EMPLOYEE")
    print("========================================")
    print("1. Search by Employee ID")
    print("2. Search by Employee Name")
    print("3. Search by Employee Role")
    print("4. Exit Search")
    print("========================================")

    choice = input("Choose your search filter: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))

        query = "SELECT * FROM EMPLOYEES WHERE ID = %s"
        values = (emp_id,)

    elif choice == "2":
        print("\n1. Exact Match (Without LIKE)")
        print("2. Partial Match (With LIKE)")

        search_choice = input("Choose search type: ")
        emp_name = input("Enter Employee Name: ")

        if search_choice == "1":
            query = "SELECT * FROM EMPLOYEES WHERE NAME = %s"
            values = (emp_name,)

        elif search_choice == "2":
            query = "SELECT * FROM EMPLOYEES WHERE NAME LIKE %s"
            values = ("%" + emp_name + "%",)

        else:
            print("Invalid search type!")
            cursor.close()
            conn.close()
            return

    elif choice == "3":
        print("\n1. Exact Match (Without LIKE)")
        print("2. Partial Match (With LIKE)")

        search_choice = input("Choose search type: ")
        emp_role = input("Enter Employee Role: ")

        if search_choice == "1":
            query = "SELECT * FROM EMPLOYEES WHERE ROLE = %s"
            values = (emp_role,)

        elif search_choice == "2":
            query = "SELECT * FROM EMPLOYEES WHERE ROLE LIKE %s"
            values = ("%" + emp_role + "%",)

        else:
            print("Invalid search type!")
            cursor.close()
            conn.close()
            return

    elif choice == "4":
        print("Exiting Employee Search.")
        cursor.close()
        conn.close()
        return

    else:
        print("Invalid choice! Please select 1 to 4.")
        cursor.close()
        conn.close()
        return

    cursor.execute(query, values)
    employees = cursor.fetchall()

    if employees:
        print("\n========== SEARCH RESULTS ==========")

        for employee in employees:
            print(employee)
    else:
        print("No employee found for this search filter.")

    cursor.close()
    conn.close()

def delete_employee():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to delete: "))

    query = "SELECT * FROM EMPLOYEES WHERE ID = %s"
    values = (emp_id,)

    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        confirm = input("Are you sure you want to delete this employee? (yes/no): ")

        if confirm.lower() == "yes":
            query = "DELETE FROM EMPLOYEES WHERE ID = %s"
            cursor.execute(query, values)
            conn.commit()
            print("Employee deleted successfully!")

        else:
            print("Deletion cancelled.")

    else:
        print("No employee exists with this ID.")

    cursor.close()
    conn.close()