a. Load a file “employee.csv”.
-> 
    emp = LOAD 'employee.csv' USING PigStorage(',')
    AS (eno:int, ename:chararray, salary:double,
        dept:chararray, age:int);

b. Display all employees of Computer Department.
->
    computer = FILTER emp BY dept == 'Comp';
    DUMP computer;

c. Dump all employees whose age is less than 30.
->
    young = FILTER emp BY age < 30;
    DUMP young;

d. Group the above relation by department.
-> dept_group = GROUP emp BY dept;

e. Dump employee having maximum age for each department.
->
    max_age = FOREACH dept_group GENERATE
        group AS department, MAX(emp.age) AS maximum_age;
    DUMP max_age;