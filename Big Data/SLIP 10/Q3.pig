a. Load a file “employee.csv”.
-> 
    emp = LOAD 'employee.csv' USING PigStorage(',')
    AS (eno:int, ename:chararray, salary:double,
        dept:chararray, age:int);

b. Display all employees of ComputerDepartment.
-> 
    computer = FILTER emp BY dept == 'Comp';
    DUMP computer;

c. Dump all employees whose age is lessthan 30.
-> 
    young = FILTER emp BY age < 30;
    DUMP young;

d. Group the above relation by department.
-> 
    dept_group = GROUP emp BY dept;
    DUMP dept_group;

e. Dump employee having maximumage.
->
    max_age = FOREACH dept_group GENERATE group AS department, MAX(emp.age) AS maximum_age;

    DUMP max_age;
