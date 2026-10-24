
<h1 align="center">Employee Task Tracking System</h1>

<p align="center">
  A Python and MySQL-based application for managing employees, tasks, assignments, and task progress.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
  The Employee Task Tracking System is designed to simplify employee and task management.
  It provides two panels: an Admin Panel and an Employee Panel.
  Admins can manage employees, tasks, and assignments, while employees can view their assigned tasks,
  update task status, and add comments.
</p>

<h2>✨ Features</h2>

<h3>👨‍💼 Admin Panel</h3>

<ul>
  <li>Add, view, update, search, and delete employees.</li>
  <li>Create, view, update, search, and delete tasks.</li>
  <li>Filter tasks by status and priority.</li>
  <li>View overdue tasks.</li>
  <li>Assign tasks to employees.</li>
  <li>View task assignments.</li>
  <li>View tasks assigned to specific employees.</li>
  <li>Reassign tasks and remove assignments.</li>
  <li>View reports and analytics.</li>
</ul>

<h3>👨‍💻 Employee Panel</h3>

<ul>
  <li>View personal profile.</li>
  <li>View assigned tasks.</li>
  <li>Update the status of assigned tasks.</li>
  <li>Add comments to assigned tasks.</li>
  <li>View completed tasks.</li>
  <li>Logout from the employee panel.</li>
</ul>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li><strong>Programming Language:</strong> Python</li>
  <li><strong>Database:</strong> MySQL</li>
  <li><strong>Database Connector:</strong> MySQL Connector/Python</li>
  <li><strong>Code Editor:</strong> Visual Studio Code</li>
  <li><strong>Database Tool:</strong> MySQL Workbench</li>
  <li><strong>Version Control:</strong> Git and GitHub</li>
</ul>

<h2>📂 Project Structure</h2>

<pre>
EmployeeTaskTrackingSystem/
│
├── main.py
├── admin.py
├── employee_panel.py
├── employee.py
├── task.py
├── assignment.py
├── comments.py
├── reports.py
├── db_connection.py
├── requirements.txt
└── README.md
</pre>

<h2>⚙️ Requirements</h2>

<ul>
  <li>Python 3</li>
  <li>MySQL Server</li>
  <li>MySQL Workbench (optional)</li>
  <li>Required Python packages</li>
</ul>

<h2>🚀 Installation and Setup</h2>

<h3>Step 1: Clone the Repository</h3>

<pre>
git clone https://github.com/Chandrasekhar152/Employee-Task-Tracking-System.git
</pre>

<h3>Step 2: Navigate to the Project Folder</h3>

<pre>
cd Employee-Task-Tracking-System
</pre>

<h3>Step 3: Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>Step 4: Create the Database</h3>

<p>Open MySQL Workbench and execute:</p>

<pre>
CREATE DATABASE employee_task_management;

USE employee_task_management;
</pre>

<p>
  Create the following tables using your project's SQL queries:
</p>

<ul>
  <li>EMPLOYEES</li>
  <li>tasks</li>
  <li>assigned_tasks</li>
  <li>comments</li>
</ul>

<h3>Step 5: Configure the Database Connection</h3>

<p>
  Open <code>db_connection.py</code> and configure your MySQL connection
  using your local database credentials.
</p>

<pre>
import mysql.connector

def db_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="employee_task_management"
    )
    return conn
</pre>

<p>
  <strong>Note:</strong> Replace the example username and password with your own credentials.
  Never upload your actual database password to GitHub.
</p>

<h3>Step 6: Run the Application</h3>

<pre>
python main.py
</pre>

<p>
  Select the Admin Panel or Employee Panel from the main menu to access the available features.
</p>

<h2>🗄️ Database Tables</h2>

<table>
  <tr>
    <th>Table Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>EMPLOYEES</td>
    <td>Stores employee information.</td>
  </tr>
  <tr>
    <td>tasks</td>
    <td>Stores task details, priorities, due dates, and statuses.</td>
  </tr>
  <tr>
    <td>assigned_tasks</td>
    <td>Stores task assignments to employees.</td>
  </tr>
  <tr>
    <td>comments</td>
    <td>Stores comments associated with tasks and employees.</td>
  </tr>
</table>

<h2>🔐 Authorization</h2>

<p>
  Employees can access their assigned tasks and perform permitted actions.
  The application checks task assignments before allowing employees to update task status
  or add comments.
</p>

<p>
  <strong>Note:</strong> Employee ID input alone does not provide secure authentication.
  Password-based login and additional security checks are recommended before production use.
</p>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>Implement secure admin and employee login.</li>
  <li>Add password hashing and authentication.</li>
  <li>Develop a graphical or web-based interface.</li>
  <li>Add email notifications for task assignments and deadlines.</li>
  <li>Improve reports and analytics.</li>
  <li>Add input validation and error handling.</li>
</ul>

<h2>👨‍💻 Author</h2>

<p>
  <strong>Chandra Sekhar Sadhu</strong><br>
  B.Tech in Artificial Intelligence and Machine Learning
</p>

<h2>📄 License</h2>

<p>
  This project was developed for learning and educational purposes.
</p>
