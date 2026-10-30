# Consider the Movie Data set. Write a Map Reduce program to find average rating per Movie.

from mrjob.job import MRJob

class MRAverageMovieRating(MRJob):
    def mapper(self, key, line):
        (userID, movieID, rating, timestamp) = line.split("\t")
        yield movieID, float(rating)

    def reducer(self, movieID, ratings):
        total = 0
        count = 0

        for rating in ratings:
            total += rating
            count += 1

        average = total / count
        yield movieID, average

if __name__ == '__main__':
    MRAverageMovieRating.run()