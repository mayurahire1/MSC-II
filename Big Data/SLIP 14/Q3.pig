a. Load the file “Movie.csv”.
-> 
    movies = LOAD 'Movie.csv' USING PigStorage(',')
    AS (Movie_id:int, M_title:chararray, Release_year:int,
        Votes:int, score:double);

b. Dump the titles of movies that have more than 100 votes.
->
    popular = FILTER movies BY Votes > 100;
    titles = FOREACH popular GENERATE M_title;
    DUMP titles;

c. Dump the title and votes of movies madein year 2020.
->
    movies_2020 = FILTER movies BY Release_year == 2020;
    result = FOREACH movies_2020 GENERATE M_title, Votes;
    DUMP result;

d. Display the votes and score of the movie“Bhoot”
->
    bhoot = FILTER movies BY M_title == 'Bhoot';
    result_bhoot = FOREACH bhoot GENERATE Votes, score;
    DUMP result_bho

e. Group Movie relation by votes
->
    grouped = GROUP movies BY Votes;
    DUMP grouped;
