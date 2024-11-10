CREATE DATABASE Employees;

CREATE TABLE Employees (Name VARCHAR(50),
						Position VARCHAR(150),
						Department VARCHAR(120),
						Salary INT);

INSERT INTO Employees (Name, Position, Department, Salary)
VALUES ('Ilya Shimanko', 'developer', 'development', 4000),
		('Nickolay Efremov', 'manager', 'marketing', 6000),
		('Alexandr Petrov','salesman','sales',7500);
		

UPDATE Employees SET Position='main-salesman' WHERE Name='Alexandr Petrov';

alter table employees add column HireDate DATE;

update employees set Hiredate='June 30, 2023' where Name='Alexandr Petrov';
update employees set Hiredate='July 13, 2021' where Name='Ilya Shimanko';
update employees set Hiredate='October 22, 2022' where Name='Nickolay Efremov';

select Name from employees where position='manager';

select Name from employees where Salary>5000;

select Name from employees where department ='sales';

select AVG(Salary) as AvgSalary from employees;

DROP TABLE Employees;

