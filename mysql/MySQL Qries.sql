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
create table Courses (
	course_id int primary key auto_increment,
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
select * from courses;
insert into Enrollments(student_id, course_id) values(2,103); 
# ==== Need to clarify doubt here.. Not able to add record for the above one ====
select * from Enrollments;
update Courses set course_name=null where course_id=103;

