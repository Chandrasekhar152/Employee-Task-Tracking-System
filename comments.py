import mysql.connector as db

conn = db.connect(
    user='root',
    password='YOUR_PASSWORD',
    host='localhost',
    database='vcubemysql'
)

cursor = conn.cursor()

# Display all employees
cursor.execute('SELECT * FROM employee')
result = cursor.fetchall()
print(result)

# Update the salary
cursor.execute(
    'UPDATE employee SET salary = 300000 WHERE employee_id = 1'
)
conn.commit()

# Display the updated employee
cursor.execute(
    'SELECT * FROM employee WHERE employee_id = 1'
)
result = cursor.fetchone()
print(result)

# Close the cursor and connection
cursor.close()
conn.close()