// Command to start hive
-> sh /home/cslogin/test/start_hive.sh

a. Create a database with the name “Udetails”
-> CREATE DATABASE Udetails;

b. Use the above created Database.
-> USE Udetails;

c. Create a table UserData with the fields (uid, name, age, gender, occupation, zipcode) where fields are terminated by “ , ”.
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

d. Load data from local storage in the path
->  LOAD DATA LOCAL INPATH '/UData.txt' INTO TABLE UserData;

f. Find number of users for each age
->
    SELECT age, COUNT(*)
    FROM UserData
    GROUP BY age;

g. Add a column email_id to the above table
-> ALTER TABLE UserData ADD COLUMNS (email_id STRING);