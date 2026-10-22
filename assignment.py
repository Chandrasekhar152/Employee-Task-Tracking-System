import db_connection

def assign_task():

    assignment_id = int(input('Enter assigenment_id: '))
    task_id = int(input('Enter task id: '))
    employee_id = int(input('Enter employee id: '))

    conn = db_connection.db_conn()
    cursor = conn.cursor()
    query = 'INSERT INTO assigned_tasks (assignment_id, task_id, employee_id, assigned_date) VALUES( %s, %s, %s, NOW() )'
    values = (assignment_id, task_id, employee_id)
    cursor.execute(query, values)
    conn.commit()
    print("Task assigned successfully!")

    cursor.close()
    conn.close()

def view_assignments():
    conn = db_connection.db_conn()
    cursor = conn.cursor()
    query = 'SELECT * FROM assigned_tasks'
    cursor.execute(query)
    
    assignments = cursor.fetchall()
    for assignment in assignments:
        print(assignment)
        
    cursor.close()
    conn.close()