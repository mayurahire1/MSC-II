a. Load the file “employee.csv”
-> 
    emp = LOAD 'employee.csv' USING PigStorage(',')
    AS (eno:int, ename:chararray, salary:double,
        dept:chararray, age:int);
    
b. Display employee having maximum age.
->
    ordered_age = ORDER emp BY age DESC;
    oldest = LIMIT ordered_age 1;
    DUMP oldest;

c. Dump department wise sum of salary.
->
    dept_group = GROUP emp BY dept;
    dept_salary = FOREACH dept_group GENERATE
        group AS department, SUM(emp.salary) AS total_salary;
    DUMP dept_salary;

d. Dump all employees according to descending order of employee name.
->
    ordered_name = ORDER emp BY ename DESC;
    DUMP ordered_name;

e. Display employees of Sales department
->
    sales = FILTER emp BY dept == 'Sales';
    DUMP sales;