import mysql.connector
from mysql.connector import Error

def create_database_and_connect(host_name, user_name, password, db_name):
    try:
        # Connect without specifying a database to create one if it doesn't exist
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.close()
        connection.close()
    except Error as e:
        print("Error:", e)
        
def create_tables_and_insert_records(host_name, user_name, password, db_name):
    try:
        # Now connect to the specific database
        connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=password,
        database=db_name
        )
        cursor = connection.cursor(buffered=True)

        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                dep_id INT PRIMARY KEY AUTO_INCREMENT,
                dep_name VARCHAR(32)
                )
            """)
        
        # Insert into departments (use parameterized queries)
        # Note: for single tuple, put comma at the end of the value (value,)
        # ===== Example: ======
        # departments = ['HR', 'IT', 'Finance', 'Marketing']
        # for dep in departments:
            # cursor.execute("INSERT INTO departments (dep_name) VALUES (%s)", (dep,))
        # =====================

        # ======= cursor.executemany() is used to execute same sql statement multiple times. =======
        # Example:
        departments = [(101,'HR'), (102,'IT'), (103,'Finance'), (104,'Marketing')]
        cursor.executemany("INSERT INTO departments(dep_id,dep_name) VALUES(%s,%s)",departments)

        cursor.execute("select * from departments")
        departments_data = cursor.fetchall()
        print(departments_data)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INT PRIMARY KEY AUTO_INCREMENT,
                emp_name VARCHAR(32),
                dep_id INT,
                FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
                )
        """)
        employees = [('Alies',101),('Bob',102),('Charlie',103),('David',104),('Emma',102)]
        cursor.executemany("INSERT INTO employees(emp_name,dep_id) VALUES(%s,%s)",employees)

        # fetch all rows
        cursor.execute("select * from employees")
        data = cursor.fetchall()
        print(data)

        # fetch one row from the table. use indexing for iterate over the row
        cursor.execute("select * from employees")
        row = cursor.fetchone()
        id = cursor.fetchone()[0]
        print('Data: ',row)
        print('id=', id)

        # fetch a particular row using where clause
        cursor.execute("select * from employees where emp_id=13")
        data = cursor.fetchall()
        print(data)

        # fetch all rows using orderby clause
        cursor.execute("select * from employees order by emp_name desc")
        data = cursor.fetchall()
        print(data)

        # update name as 'Arya' where id=11
        cursor.execute("update employees set emp_name='Arya' where emp_id=11")
        cursor.execute("select * from employees order by emp_name")
        data = cursor.fetchall()
        print(data)

        # Delete from table where id=15
        cursor.execute('delete from employees where emp_id=15')
        cursor.execute("select * from employees order by emp_name")
        data = cursor.fetchall()
        print(data)

        # Show only 2 rows
        cursor.execute("select *from employees limit 2")
        data = cursor.fetchall()
        print(data)

        # Note:
        # It should use connection.commit() at the end of the sql commands like INSERT, UPDATE, DELETE
        # It should not use connection.commit() for the SELECT command

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
            product_id INT PRIMARY KEY AUTO_INCREMENT,
            product_name VARCHAR(32),
            price DOUBLE
            )
        """)
        prod_list = [
            (201,'cello pen',15),
            (202,'wildcraft bag',600),
            (203,'Dabur honey',300),
            (204,'popy umbrella',400)
        ]
        cursor.executemany(
            "INSERT INTO products(product_id,product_name,price) VALUES(%s,%s,%s)",
            prod_list
        )

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects(
                project_id INT PRIMARY KEY AUTO_INCREMENT,
                project_name VARCHAR(32),
                dep_id INT,
                FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
            )
        """)

        project_list = [(201,'ASR',101),(202,'DSN',102),(203,'EXN',103)]
        cursor.executemany("INSERT INTO projects(project_id,project_name,dep_id) VALUES(%s,%s,%s)", 
        project_list
        )

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emp_projects(
                emp_id INT,
                project_id INT,
                FOREIGN KEY(project_id) REFERENCES projects(project_id)
            )
        """)

        # cursor.execute("ALTER TABLE emp_projects ADD CONSTRAINT FOREIGN KEY(emp_id) REFERENCES employees(emp_id)")

        emp_list = [(11,201),(12,202),(13,203)]
        cursor.executemany("INSERT INTO emp_projects(emp_id,project_id) VALUES(%s,%s)",
        emp_list
        )

        cursor.execute()

        
        connection.commit()
        print("Created tables and inserted values successfully.")
        cursor.close()
        connection.close()

    except Error as e:
        print("Error:", e)

def join_tables(host_name, user_name, password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        # Join 2 tables
        cursor.execute("select e.emp_name,d.dep_name from employees e join departments d on e.dep_id=d.dep_id")
        result = cursor.fetchall()
        for data in result:
            print(data)
            print('Employee: ',data[0], ' | Department: ',data[1])

        # Join more than 2 tables
        query = """
            select e.emp_name,p.project_name,d.dep_name from emp_projects emp right join projects p
            on emp.project_id=p.project_id right join departments d on p.dep_id=d.dep_id right join employees e
            on emp.emp_id=e.emp_id
        """


        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(f"Employee: {row[0]}, Department: {row[1]}, Project: {row[2]}")

        cursor.close()
        connection.close()

        cursor.close()
        connection.close()

    except Error as e:
        print('Error: ',e)

# Usage
create_database_and_connect("localhost","root","root123","mysql_db")
# create_tables_and_insert_records("localhost","root","root123","mysql_db")
join_tables("localhost","root","root123","mysql_db")


