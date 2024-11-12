
CREATE DATABASE employees;

CREATE TABLE employees (name VARCHAR(50),
						Position VARCHAR(150),
						department VARCHAR(120),
						salary INT);

INSERT INTO employees (name, Position, department, salary)

VALUES ('Ilya Shimanko', 'developer', 'development', 4000),
		('Nickolay Efremov', 'manager', 'marketing', 6000),
		('Alexandr Petrov','salesman','sales',7500);
		
UPDATE employees SET Position='main-salesman' WHERE name='Alexandr Petrov';

alter table employees add column HireDate DATE;

update employees set Hiredate='June 30, 2023' where name='Alexandr Petrov';
update employees set Hiredate='July 13, 2021' where name='Ilya Shimanko';
update employees set Hiredate='October 22, 2022' where name='Nickolay Efremov';

select name from employees where position='manager';

select name from employees where salary>5000;

select name from employees where department ='sales';

select AVG(salary) as AvgSalary from employees;

DROP TABLE employees;


