a. Load a file “employee.csv”
-> 
    emp = LOAD 'employee.csv' USING PigStorage(',')
    AS (eno:int, ename:chararray, salary:double,
        dept:chararray, age:int);

b. Group the above relation by salary.
->
    salary_group = GROUP emp BY salary;
    DUMP salary_group;

c. Display all employees of ComputerDepartment.
->
    computer = FILTER emp BY dept == 'Comp';
    DUMP computer;

d. Display department wise sum of salary.
->
    dept_group = GROUP emp BY dept;

    dept_salary = FOREACH dept_group GENERATE
        group AS department, SUM(emp.salary) AS total_salary;

    DUMP dept_salary;

e. Dump all employees according todescending order of employee name.
-> 
    ordered = ORDER emp BY ename DESC;
    DUMP ordered;