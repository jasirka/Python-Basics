import mysql.connector
from mysql.connector import Error
def create_database(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password
        )

        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    except Error as e:
        print('Error: ',e)

def create_employees_table(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'employees'")
        result = cursor.fetchone()
        if result is None:
            cursor.execute("CREATE TABLE employees(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(32),position VARCHAR(32), salary DOUBLE)")
            print('The Employees table has been created successfully')
        else:
            print('The employees table has already been created.')
    except Error as e:
        print('Error: ',e)

def insert_records_employees_table(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        cursor.execute("delete from employees") 
        employees_data = [('Alice','Developer',60000),('Bob','Manager',80000),('Charlie','Tester',50000)]
        cursor.executemany("INSERT INTO employees(name,position,salary) VALUES(%s,%s,%s)",employees_data)
        connection.commit()
        print('The Employee records were inserted successfully.')
    except Error as e:
        print('Error: ',e)

def select_all_records_from_employees_table(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        print("Name |  Position |  Salary")
        for row in result:
            print(f"{row[1]} | {row[1]} | {row[2]}")
    
    except Error as e:
        print('Error: ',e)

def update_salary_of_bob(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        cursor.execute("UPDATE employees SET salary=85000 WHERE name='Bob'")
        connection.commit()
        print("Salary of Bob was updated successfully")

    except Error as e:
        print('Error: ',e)

def delete_record_of_charlie(ost_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        check_qry = "SELECT * FROM employees WHERE name='Charlie'"
        cursor.execute(check_qry)
        result = cursor.fetchone()
        if result:
            delete_qry = "DELETE FROM employees WHERE name='Charlie'"
            cursor.execute(delete_qry)
            print("Record of Charlie was deleted successfully")
        else:
            print("Record of Charlie was already deleted")

    except Error as e:
        print('Error: ',e)

# My SQL details
host_name = "localhost"
user_name = "root"
password = "root123"
database = "company"
# create_database(host_name, user_name, password, database)
# create_employees_table(host_name, user_name, password, database)
# insert_records_employees_table(host_name, user_name, password, database)
# select_all_records_from_employees_table(host_name, user_name, password, database)
update_salary_of_bob(host_name, user_name, password, database)
delete_record_of_charlie(host_name, user_name, password, database)