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