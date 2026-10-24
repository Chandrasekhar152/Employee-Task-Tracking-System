import db_connection

def add_comment(employee_id):
    conn = db_connection.db_conn()
    cursor = conn.cursor()

    task_id = int(input("Enter Task ID: "))

    query = "SELECT * FROM assigned_tasks WHERE task_id = %s AND employee_id = %s"
    cursor.execute(query, (task_id, employee_id))

    result = cursor.fetchone()

    if result:
        comment_text = input("Enter your comment: ")

        query = """
        INSERT INTO comments (task_id, employee_id, comment_text, created_at)
        VALUES (%s, %s, %s, NOW())
        """

        cursor.execute(query, (task_id, employee_id, comment_text))
        conn.commit()

        print("Comment added successfully!")

    else:
        print("This task is not assigned to you.")

    cursor.close()
    conn.close()