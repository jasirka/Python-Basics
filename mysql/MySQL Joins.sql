use python_workbench;
insert into orders(order_id,pid,customerid) values('ord4323009','prd003','cust003');
create table customer(customerid varchar(32), cust_name varchar(32), email varchar(32), mobno varchar(32));
insert into customer(customerid,cust_name,email,mobno) values('cust003','Giri Pai','giripai99@yopmail.com','8932000000');
# Inner Join
select c.cust_name, c.email, c.mobno, p.pname, p.price, o.quantity, (p.price * o.quantity) as total_price from customer c INNER JOIN orders o ON c.customerid=o.customerid INNER JOIN products p ON o.pid=p.pid;
# Left Join
select c.cust_name, c.email, c.mobno, p.pname, p.price, o.quantity, (p.price * o.quantity) as total_price from customer c  LEFT JOIN orders o ON c.customerid=o.customerid LEFT JOIN products p ON o.pid=p.pid;
# Right Join
select c.cust_name, c.email, c.mobno, p.pname, p.price, o.quantity, (p.price * o.quantity) as total_price from customer c  RIGHT JOIN orders o ON c.customerid=o.customerid RIGHT JOIN products p ON o.pid=p.pid;
# ORDER BY 
select c.cust_name, c.email, c.mobno, p.pname, p.price, o.quantity, (p.price * o.quantity) as total_price from customer c INNER JOIN orders o ON c.customerid=o.customerid INNER JOIN products p ON o.pid=p.pid order by c.cust_name;

create table employee(empid int not null auto_increment,ename varchar(20), mobno varchar(20), email varchar(32), primary key(empid));
ALTER TABLE employee_salary MODIFY empid INT; # Removes auto increment
alter table employee_salary drop primary key; # Removes primary key
DELETE FROM employee_salary
WHERE empid NOT IN (SELECT empid FROM employee);
alter table employee_salary add constraint FK_esalary foreign key(empid) references employee(empid);
select * from employee_salary;

select ename,sum(HRA+DA+TA) as total_income, sum(PF+employee_tax) as deductions, sum(HRA+DA+TA)  - sum(PF+employee_tax) as net_income from employee emp inner join employee_salary emp_sal
on emp.empid=emp_sal.empid group by ename;
