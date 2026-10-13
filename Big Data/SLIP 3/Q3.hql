1. Create a database with the name “Udetails”
-> CREATE DATABASE Udetails;

2. Use the above created Database.
-> USE Udetails;

3. Create a table UserData with the fields (uid, name, age, gender, occupation, zipcode) where fields are terminated by “ , ”.
->
    CREATE TABLE UserData (
        uid INT,
        name STRING,
        age INT,
        gender STRING,
        occupation STRING,
        zipcode STRING
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ',';

4. Load data from local storage in the path
->  LOAD DATA LOCAL INPATH '/UData.txt' INTO TABLE UserData;

5. Find average age of all females.
-> 
    SELECT AVG(age)
    FROM UserData
    WHERE LOWER(gender) = 'female';

6. Find number of users for each age
->
    SELECT age, COUNT(*)
    FROM UserData
    GROUP BY age
    ORDER BY age;