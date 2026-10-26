1. Create a database with the name IRating
-> CREATE DATABASE IRating;

2. Use the above created database
-> USE IRating;

3. Create table Rating with the fields(userid, item_id, rating, timestamp) where fields are terminated by ‘\t’
-> 
    CREATE TABLE Rating (
        userid INT,
        item_id INT,
        rating FLOAT,
        timestamp BIGINT
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY '\t';

4. Load data from local storage in the path home/user/data/Item_Rating”
-> 
    LOAD DATA LOCAL INPATH '/Item_Rating'
    INTO TABLE Rating;

5. Display first 100 rows of the table
->  SELECT * FROM Rating LIMIT 100;

6. List the Item_id of all items which have received rating greater than 4
-> 
    SELECT DISTINCT item_id
    FROM Rating
    WHERE rating > 4;