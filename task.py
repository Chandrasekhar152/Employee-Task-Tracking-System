import db_connection

def create_task():
    task_id = int(input("Enter task ID: "))
    task_title = input()
    task_description = input()
    task_priority = input('Choose (High, Medium , Low)').capitalize()
    task_due_date = input('Enter in this format only: YYYY-MM-DD')
    task_status = input("Choose (Pending, In Progress, Completed)").title()
    

    if ((task_priority == 'High') or (task_priority == 'Medium') or (task_priority == 'Low')) and ((task_status == 'Pending') or (task_status == 'In Progress') or (task_status == 'Completed')):
        conn = db_connection.db_conn()
        cursor = conn.cursor()

        query = 'INSERT INTO tasks(task_id, title, description, priority, due_date, status, created_at) VALUES (%s, %s, %s, %s, %s, %s, NOW())'
        values = (task_id, task_title, task_description, task_priority, task_due_date, task_status)
        cursor.execute(query,values)

        conn.commit()
        print("Task created successfully!")
        cursor.close()
        conn.close()

    else:
        print("Invalid priority or status. Please try again.")
        create_task()

def view_task():
    conn = db_connection.db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()
    for task in tasks:
        print(task)
    
    cursor.close()
    conn.close()

def delete_task():

    conn = db_connection.db_conn()
    cursor = conn.cursor()
    
    print("\n1. Delete by Task ID")
    print("2. Delete by Status")
    print("3. Delete by Task ID and Status")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task_id = int(input("Enter Task ID: "))
    
        query = "DELETE FROM tasks WHERE task_id = %s"
        values = (task_id,)
    
    elif choice == "2":
        status = input("Enter task status: ").strip().title()
    
        query = "DELETE FROM tasks WHERE status = %s"
        values = (status,)
    
    elif choice == "3":
        task_id = int(input("Enter Task ID: "))
        status = input("Enter task status: ").strip().title()
    
        query = "DELETE FROM tasks WHERE task_id = %s AND status = %s"
        values = (task_id, status)
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        cursor.close()
        conn.close()
        return
    
    confirm = input("Are you sure you want to delete? (yes/no): ")
    
    if confirm.lower() == "yes":
        cursor.execute(query, values)
    
        if cursor.rowcount > 0:
            conn.commit()
            print("Task deleted successfully!")
        else:
            print("No matching task found.")
    
    else:
        print("Deletion cancelled.")
    
    cursor.close()
    conn.close()

def filter_tasks_by_status():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    status = input('Enter the status (Pending, In Progress, Completed): ').strip().title()

    query = 'SELECT * FROM tasks WHERE status = %s'
    value = (status,)

    cursor.execute(query, value)
    results = cursor.fetchall()

    if results:
        for result in results:
            print(result)
    else:
        print("No tasks found with this status.")

    cursor.close()
    conn.close()


def filter_tasks_by_priority():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    priority = input('Enter the priority (High, Medium, Low): ').strip().title()

    query = 'SELECT * FROM tasks WHERE priority = %s'
    value = (priority,)

    cursor.execute(query, value)
    results = cursor.fetchall()

    if results:
        for result in results:
            print(result)
    else:
        print("No tasks found with this priority.")

    cursor.close()
    conn.close()


def search_task():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    print("\n========== SEARCH TASK ==========")
    print("1. Search by Task ID")
    print("2. Search by Task Title")
    print("3. Exit Search")

    choice = input("Choose your search filter: ")

    if choice == "1":
        task_id = int(input("Enter Task ID: "))
        query = "SELECT * FROM tasks WHERE task_id = %s"
        values = (task_id,)

    elif choice == "2":
        print("\n1. Exact Match")
        print("2. Partial Match")

        search_choice = input("Choose search type: ")
        title = input("Enter Task Title: ")

        if search_choice == "1":
            query = "SELECT * FROM tasks WHERE title = %s"
            values = (title,)

        else:
            query = "SELECT * FROM tasks WHERE title LIKE %s"
            values = ("%" + title + "%",)

    else:
        print("Exiting Task Search.")
        cursor.close()
        conn.close()
        return

    cursor.execute(query, values)
    results = cursor.fetchall()

    if results:
        print("\n========== SEARCH RESULTS ==========")

        for result in results:
            print(result)

    else:
        print("No tasks found.")

    cursor.close()
    conn.close()

def update_task():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    task_id = int(input("Enter Task ID to update: "))

    query = "SELECT * FROM tasks WHERE task_id = %s"
    values = (task_id,)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        print("\nTask Details:")
        print(result)

        print("\nWhat do you want to update?")
        print("1. Task Title")
        print("2. Task Description")
        print("3. Task Priority")
        print("4. Task Due Date")
        print("5. Task Status")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_value = input("Enter new task title: ")
            query = "UPDATE tasks SET title = %s WHERE task_id = %s"

        elif choice == "2":
            new_value = input("Enter new task description: ")
            query = "UPDATE tasks SET description = %s WHERE task_id = %s"

        elif choice == "3":
            new_value = input("Enter new priority (High, Medium, Low): ").strip().title()
            query = "UPDATE tasks SET priority = %s WHERE task_id = %s"

        elif choice == "4":
            new_value = input("Enter new due date (YYYY-MM-DD): ")
            query = "UPDATE tasks SET due_date = %s WHERE task_id = %s"

        elif choice == "5":
            new_value = input("Enter new status (Pending, In Progress, Completed): ").strip().title()
            query = "UPDATE tasks SET status = %s WHERE task_id = %s"

        else:
            print("Invalid choice!")
            cursor.close()
            conn.close()
            return

        values = (new_value, task_id)
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("Task updated successfully!")
        else:
            print("No changes were made to the task.")

    else:
        print("Task ID not found!")

    cursor.close()
    conn.close()

def view_overdue_tasks():
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    query = """
        SELECT task_id, title, description, priority, due_date, status
        FROM tasks
        WHERE due_date < CURDATE()
        AND status != 'Completed'
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n========== OVERDUE TASKS ==========")

    if results:
        for result in results:
            print("Task ID:", result[0])
            print("Task Title:", result[1])
            print("Description:", result[2])
            print("Priority:", result[3])
            print("Due Date:", result[4])
            print("Status:", result[5])
            print("-----------------------------------")
    else:
        print("No overdue tasks found.")

    cursor.close()
    conn.close()

def view_my_tasks_id(employee_id):
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    query = """
        SELECT tasks.task_id, tasks.title, tasks.description,
               tasks.priority, tasks.due_date, tasks.status
        FROM tasks
        JOIN assigned_tasks
            ON tasks.task_id = assigned_tasks.task_id
        WHERE assigned_tasks.employee_id = %s
    """

    value = (employee_id,)

    cursor.execute(query, value)
    results = cursor.fetchall()

    print("\n========== MY TASKS ==========")

    if results:
        for result in results:
            print("Task ID:", result[0])
            print("Task Title:", result[1])
            print("Description:", result[2])
            print("Priority:", result[3])
            print("Due Date:", result[4])
            print("Status:", result[5])
            print("------------------------------")
    else:
        print("No tasks assigned to you.")

    cursor.close()
    conn.close()


def update_task_status_id(employee_id):
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    task_id = int(input("Enter Task ID: "))

    query = """
        SELECT task_id
        FROM assigned_tasks
        WHERE task_id = %s AND employee_id = %s
    """

    cursor.execute(query, (task_id, employee_id))
    result = cursor.fetchone()

    if result:
        print("\nSelect New Status:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Completed")

        choice = input("Enter your choice: ")

        if choice == "1":
            status = "Pending"
        elif choice == "2":
            status = "In Progress"
        elif choice == "3":
            status = "Completed"
        else:
            print("Invalid choice!")
            cursor.close()
            conn.close()
            return

        query = """
            UPDATE tasks
            SET status = %s
            WHERE task_id = %s
        """

        cursor.execute(query, (status, task_id))
        conn.commit()

        print("Task status updated successfully!")

    else:
        print("You are not authorized to update this task.")
        print("The task may not exist or may not be assigned to you.")

    cursor.close()
    conn.close()

def view_completed_tasks(employee_id):
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    query = """
    SELECT tasks.*
    FROM tasks
    JOIN assigned_tasks
    ON tasks.task_id = assigned_tasks.task_id
    WHERE assigned_tasks.employee_id = %s
    AND tasks.status = 'Completed'
    """

    cursor.execute(query, (employee_id,))
    results = cursor.fetchall()

    if results:
        print("\n========== COMPLETED TASKS ==========")

        for result in results:
            print(result)

    else:
        print("No completed tasks found.")

    cursor.close()
    conn.close()