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


def view_tasks_by_employee():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    employee_id = int(input('Enter the Employee ID: '))

    query = 'SELECT NAME FROM EMPLOYEES WHERE ID = %s'
    value = (employee_id,)

    cursor.execute(query, value)
    name = cursor.fetchone()

    print('\n========== VIEW TASKS BY EMPLOYEE ==========')
    print('Employee ID:', employee_id)

    if name:
        print('Employee Name:', name[0])
        print()

        query = """
            SELECT tasks.task_id,
                   tasks.title,
                   tasks.description,
                   tasks.priority,
                   tasks.status
            FROM EMPLOYEES
            JOIN assigned_tasks
                ON EMPLOYEES.id = assigned_tasks.employee_id
            JOIN tasks
                ON assigned_tasks.task_id = tasks.task_id
            WHERE assigned_tasks.employee_id = %s
        """

        cursor.execute(query, value)
        results = cursor.fetchall()

        if results:
            for result in results:
                print('Task ID:', result[0])
                print('Task Title:', result[1])
                print('Description:', result[2])
                print('Priority:', result[3])
                print('Status:', result[4])
                print('-----------------------------------')
        else:
            print('This employee has no assigned tasks.')

    else:
        print('Employee ID not found.')

    cursor.close()
    conn.close()
