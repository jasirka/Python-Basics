create database joinDb;
use joindb;
create table departments(dep_id int primary key auto_increment, dep_name varchar(32));
create table employees(emp_id int primary key auto_increment,emp_name varchar(32),dep_id int, 
foreign key(dep_id) references departments(dep_id));
insert into departments(dep_name) values('Marketing');
insert into employees(emp_name,dep_id) values('Emma',102);
insert into employees(emp_name,dep_id) values(null,103);
select *from employees;
-- 1. Write a query to display all employees along with their department names.
select emp_name, dep_name from employees e inner join departments d on e.dep_id=d.dep_id order by emp_name;
-- List employee names working in the 'IT' department.
select emp_name, dep_name from employees e inner join departments d on e.dep_id=d.dep_id and dep_name='IT' order by emp_name;
-- Display all department names along with the number of employees in each department (only
-- those with employees).
select dep_name, count(emp_name) as total_employees from employees e inner join departments d on e.dep_id=d.dep_id group by d.dep_id;
-- 2. List all employees and their department names, including employees who don’t belong to any
-- department.
select e.emp_name, d.dep_name from employees e left join departments d on e.dep_id = d.dep_id order by e.dep_id;
-- List all departments and the employees in them (show department names even if there are no
-- employees).
select e.emp_name,d.dep_name from employees e right join departments d on e.dep_id=d.dep_id order by e.dep_id;
-- 3.Show all departments and the names of their employees (include departments with no employees).
-- • List all departments, even if no employees are assigned.
select e.emp_name,d.dep_name from departments d left join employees e on d.dep_id=e.dep_id order by e.emp_id;
-- Display all employees and departments, even if they don't have matching records (use UNION
-- of LEFT and RIGHT JOIN).
select e.emp_name,d.dep_name from employees e left join department d on e.dep_id=d.dep_id union 
select e.emp_name,d.dep_name from employees e right join department d on e.dep_id=d.dep_id order by e.dep_id;
create table projects(project_id int primary key auto_increment, project_name varchar(32), dep_id int, foreign key(dep_id) references departments(dep_id));
create table emp_projects(emp_id int, project_id int, foreign key(emp_id) references employees(emp_id), foreign key(project_id) references projects(project_id));
insert into projects(project_name, dep_id) values('Budget Planner', 103);
insert into emp_projects(emp_id, project_id) values(4, 3);
-- List all projects and the names of employees working on them. Include projects with no
-- assigned employees.
select e.emp_name, p.project_name from projects p left join emp_projects ep on p.project_id=ep.project_id
left join employees e on ep.emp_id=e.emp_id order by e.emp_name;
-- List all employees along with the projects they are involved in. Include employees with no
-- projects.
select e.emp_name, p.project_name from projects p right join emp_projects ep on p.project_id=ep.project_id
right join employees e on ep.emp_id=e.emp_id order by e.emp_name;
-- Find the total number of employees involved in each project.
select p.project_name, count(e.emp_name) from projects p join emp_projects em on p.project_id=em.project_id
join employees e on em.emp_id=e.emp_id group by p.project_name;
-- Show project names along with the department name and employees working on the project.
select p.project_name, d.dep_name, e.emp_name from projects p join emp_projects emp on p.project_id=emp.project_id join 
departments d on p.dep_id=d.dep_id join employees e on e.emp_id=emp.emp_id order by e.emp_name;

-- Create the following tables with appropriate data types and constraints:
create table customers(customer_id int primary key auto_increment,name varchar(32),email varchar(32));
create table products(product_id int primary key auto_increment,product_name varchar(32),price double);
create table orders(order_id int primary key auto_increment,customer_id int,order_date date,total_amount double,
foreign key(customer_id) references customers(customer_id));
create table order_items(order_item_id int primary key auto_increment,order_id int,product_id int,quantity double);
alter table order_items add constraint frk_order foreign key(order_id) references orders(order_id),
add constraint frk_prd foreign key(product_id) references products(product_id);
-- Insert at least 3 customers, 4 products, 5 orders, and 8 order items with realistic data.
insert into customers(name,email) values('Jeni','jeni@testmail.com');
insert into products(product_name,price) values('popy umbrella',400);
insert into orders(customer_id,order_date,total_amount) values(102,'2022-08-07',350.0);
insert into order_items(order_item_id,order_id,product_id,quantity) values(408,303,204,3);
select * from order_items;
-- Write a query to display all customers.
select name,email from customers;
-- Write a query to display all products priced above $500.
select product_name,price from products where price > 500;
select * from products;
-- Write a query to show all orders placed on a specific date (choose a date you inserted).
select c.name as Customer,p.product_name as Product,o.order_date,o.total_amount from order_items i join orders o on i.order_id=o.order_id 
join products p on p.product_id=i.product_id
join customers c on c.customer_id=o.customer_id
where o.order_date='2022-08-17'
order by c.name;

select *from departments;

use mysql_db;
select * from employees;
select * from emp_projects;
select * from projects;
select * from departments;