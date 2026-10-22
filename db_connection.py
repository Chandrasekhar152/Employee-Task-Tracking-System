import mysql.connector as db

def db_conn():
    conn = db.connect(
        host = "localhost",
        user = "root",
        password = "Satyn152@gfg",
        database="employee_task_management"
    )

    return conn