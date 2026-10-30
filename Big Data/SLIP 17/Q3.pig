a. Write a pig statement to load a file “student_data.txt” containing the fields (id, firstname, lastname, age, phone, city) where fields are separated by “,”.
->
    students = LOAD 'student_data.txt' USING PigStorage(',')
    AS (id:int, firstname:chararray, lastname:chararray,
        age:int, phone:chararray, city:chararray);

b. Display the above loaded relation on to the screen
-> DUMP students;

c. Describing the relation
-> DESCRIBE students;

d. Group the above created relation by age
->  age_group = GROUP students BY age;
    DUMP age_group;

e. Group the above relation by all columns
->
    all_group = GROUP students BY
        (id, firstname, lastname, age, phone, city);
    DUMP all_group;

f. Find city wise average age
->
    city_group = GROUP students BY city;
    city_avg = FOREACH city_group GENERATE
        group AS city_name, AVG(students.age) AS average_age;
    DUMP city_avg;

