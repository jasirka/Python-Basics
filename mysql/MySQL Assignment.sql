create database StudentDB;
use StudentDB;
create table students
(
student_id int primary key,
name varchar(32),
email varchar(32),
dob date
);
alter table students add column phone varchar(16);
alter table students modify column name varchar(100);
alter table students drop column phone;
insert into students(student_id,name,email,dob)
values(105,'Rinu Antony','rinu.antony@yopmail.com','1990-08-03');
update students set email='benny.george@yopmail.com' where student_id=3;
select * from students where dob>'2000-12-31';
select name,email from students where dob>'2000-12-31';
select * from students;
delete from students where student_id=102;
delete from students where name like '%p%';
create table marks
(
foreign key(student_id) references student_id(students),
subject varchar(32),
marks int
);

insert into marks(student_id,subject,marks) values(103,'Social Science',68);
select name from students where student_id in (select student_id from marks where marks > 70);
select student_id,max(marks) as Max_Marks,min(marks) as Min_Marks,avg(marks) as Avg_Marks from marks where student_id in (select student_id from students) group by student_id;
select * from marks;
select * from students order by name;
select * from students where dob between '2000-01-01' and '2005-12-31';
select * from students where name like 'J%' or name like '%an%';
CREATE TABLE Courses (
	course_id int PRIMARY KEY AUTO_INCREMENT,
	course_name varchar(32) not null
);
insert into Courses(course_id, course_name) values(103, 'Data Science');
CREATE TABLE Enrollments (
    enroll_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
insert into Enrollments(student_id, course_id) values(5,103); 
select * from Enrollments;
update Courses set course_name=null where course_id=103;
update Enrollments set student_id=10 where enroll_id=4;
-- Create a table Employees with fields: emp_id, emp_name, salary, dept.
CREATE TABLE Employees (
	emp_id int primary key auto_increment, 
    emp_name varchar(32), 
    salary double, 
    dept varchar(32)
);
-- Alter the Employees table to:
-- • Add a column join_date (DATE).
-- • Rename the column dept to department.
-- • Drop the column salary.
-- • Drop the table Employees.
alter table Employees add column join_date date;
alter table Employees rename column dept to department;
alter table Employees drop column salary;
drop table Employees;
-- Insert 5 records into Employees, including names, departments, and join dates.
insert into Employees(emp_name, salary, department, join_date) values('Anus',40000.0,'HR department','2022-08-15');
select * from Employees;
-- Update the department of employees who joined before 2020 to ‘Operations’.
update Employees set department='Operations' where join_date < '2020-01-01';
-- Increase the salary of employees in the ‘IT’ department by 10%.
update Employees set salary= salary + salary * 10/100 where department='IT department';
-- Set the salary to NULL for employees whose name starts with ‘S’.
update Employees set salary=null where emp_name like 'S%';
-- Select employees from the 'HR' department.
select * from Employees where department='HR department';
-- Display all columns except join_date.
select emp_id,emp_name,salary,department from Employees where department='HR department';
-- Select top 3 highest-paid employees.
select * from Employees where department='HR department' order by salary desc limit 3;
-- Delete employees who have NULL in salary.
delete from Employees where salary is null;
-- Delete all records from the table without dropping the table.
delete from Employees;

-- List all sales records ordered by amount in descending order.
-- • Show sales from regions IN (‘North’, ‘West’).
-- • Select sales between 1000 and 3000.
-- • Find salespersons whose names:
-- • Start with ‘A’
-- • End with ‘n’
-- • Contain ‘an’
-- • Find employees whose name does not contain the letter ‘e’.
select *from sales;
update sales set amount=3000 where sales_id=4;
CREATE TABLE sales(
	sales_id int primary key auto_increment,
    amount double,
    region varchar(16),
    sales_person varchar(32),
    emp_name varchar(32),
    foreign key(emp_name) references employees(emp_name)
);
insert into sales(amount,region,sales_person,emp_name) values(25000,'South','Basil','Anus');
update sales set sales_person='Arun' where sales_id=2;
select * from sales where region IN ('North','West');
select * from sales where amount > 1000 and amount <3000;
select * from sales where sales_person like 'A%';


