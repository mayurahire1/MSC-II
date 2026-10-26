1. Create a database with the name StudDetail
-> CREATE DATABASE StudDetail;

2. Use the above created database.
-> USE StudDetail;

3. Create table Student with the fields(Stident_id, age, class, Subject_opted, marks ) where fields are terminated by ‘,’
-> 
    CREATE TABLE Student (
        Student_id INT,
        age INT,
        class STRING,
        Subject_opted STRING,
        marks FLOAT
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ',';

4. Load data from local storage in the path home/user/data/stud_marks”
-> 
    LOAD DATA LOCAL INPATH '/stud_marks'
    INTO TABLE Student;

5. Find the average marks per subject
->
    SELECT Subject_opted, AVG(marks)
    FROM Student
    GROUP BY Subject_opted;

6. Find subject wise maximum marks
-> 
    SELECT Subject_opted, MAX(marks)
    FROM Student
    GROUP BY Subject_opted;