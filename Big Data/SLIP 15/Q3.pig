a. Load the file “student.csv”
-> 
    students = LOAD 'student.csv' USING PigStorage(',')
    AS (Rollno:int, Sname:chararray, age:int,
        class:chararray, phone:chararray, city:chararray);

b. Write a pig script to group the above relation by age.
->
    age_group = GROUP students BY age;
    DUMP age_group;

c. Write a pig script to display all employees of ComputerDepartment.
->


d. Write a pig script do display class wise number of students.
->
    class_group = GROUP students BY class;
    class_count = FOREACH class_group GENERATE
        group AS class_name, COUNT(students) AS total_students;
    DUMP class_count;

e. Write a pig script to display all students according to descending order of student name.
->
    ordered = ORDER students BY Sname DESC;
    DUMP ordered;