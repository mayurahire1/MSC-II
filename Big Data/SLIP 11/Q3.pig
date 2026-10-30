a. Load a file “Movie.csv”.
->  
    movies = LOAD 'Movie.csv' USING PigStorage(',')
    AS (Movie_id:int, M_title:chararray, Release_year:int,
        Votes:int, score:double);

b. Dump titles of movies that havea score higher than 8.
-> 
    high_score = FILTER movies BY score > 8;

    DUMP high_score;

c. Dump the title and year of moviesmade in year 1980.
-> 
    movies_1980 = FILTER movies BY Release_year == 1980;
    result = FOREACH movies_1980 GENERATE M_title, Release_year;

    DUMP result;

d. Dump the top 5 highest vote-getting movies (use ORDER and LIMIT).
->
    ordered = ORDER movies BY Votes DESC;
    top5 = LIMIT ordered 5;
    
    DUMP top5;

e. Group Movie relation by votes
-> 
    grouped = GROUP movies BY Votes;
    DUMP grouped;