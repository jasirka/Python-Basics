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

def create_candidates_table(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES LIKE 'candidates'")
        result = cursor.fetchone()
        if result is None:
            cursor.execute("CREATE TABLE candidates(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(32),email VARCHAR(32), score DOUBLE)")
            print('The Candidates table has been created successfully')
        else:
            print('The Candidates table has already been created.')
    except Error as e:
        print('Error: ',e)

def insert_candidates_data(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        cursor.execute("delete from candidates") 
        candidates_data = [('Alice','alice@test_mail.com',70.0),('Bob','bob@test_mail.com',85.0),('Charlie','charlie@test_mail.com',75.0)]
        cursor.executemany("INSERT INTO candidates(name,email,score) VALUES(%s,%s,%s)",candidates_data)
        connection.commit()
        print('The Candidate records were inserted successfully.')
    except Error as e:
        print('Error: ',e)

def fetch_the_top_scorer(host_name, user_name, password, database):
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = database
        )

        cursor = connection.cursor()
        cursor.execute("SELECT MAX(score) FROM candidates")
        result = cursor.fetchone()
        if result:
            cursor.execute(f"SELECT * FROM candidates WHERE score={result[0]}")
            topper_data = cursor.fetchall()
            for row in topper_data:
                print("Name | Email | Score")
                print(f"{row[1]} | {row[2]} | {row[3]}")

    except Error as e:
        print('Error: ',e)

# My SQL details
host_name = "localhost"
user_name = "root"
password = "root123"
database = "test_platform"
create_database(host_name, user_name, password, database)
create_candidates_table(host_name, user_name, password, database)
insert_candidates_data(host_name, user_name, password, database)
fetch_the_top_scorer(host_name, user_name, password, database)
