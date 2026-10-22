import db_connection

def view_reports():

    conn = db_connection.db_conn()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM employees')
    employee_count = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM tasks')
    total_task = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM tasks WHERE status = "Pending" ')
    pending_tasks = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE status = "In Progress" ')
    in_progress_tasks = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE status = "Completed" ')
    completed_task = cursor.fetchone()[0]

    print(
    f'========== TASK REPORTS ==========\n'
    f'Total Employees: {employee_count}\n'
    f'Total Tasks: {total_task}\n'
    f'Pending Tasks: {pending_tasks}\n'
    f'In Progress Tasks: {in_progress_tasks}\n'
    f'Completed Tasks: {completed_task}'
    )
    cursor.close()
    conn.close()