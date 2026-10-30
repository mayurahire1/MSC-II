a. Load the data from csv file.
->
    emp = LOAD 'employee.csv' USING PigStorage(',')
    AS (eno:int, ename:chararray, salary:double,
        dept:chararray, age:int);

b. Dump all employees of Computer Department.
->
    computer = FILTER emp BY dept == 'Comp';
    DUMP computer;

c. Group the employees by department
->
    dept_group = GROUP emp BY dept;
    DUMP dept_group;

d. Dump department wise employee having maximum age.
->
    max_age = FOREACH dept_group GENERATE
        group AS department, MAX(emp.age) AS maximum_age;
    DUMP max_age;

e. Dump department wise sum of salary.
->
    dept_salary = FOREACH dept_group GENERATE
        group AS department, SUM(emp.salary) AS total_salary;
    DUMP dept_salary;