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