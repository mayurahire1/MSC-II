# Consider the Movie Data set. Write a Map Reduce program to find number of ratings per rating value.

from mrjob.job import MRJob

class MRRatingCounter(MRJob):
    def mapper(self, key, line):
        (userID, movieID, rating, timestamp) = line.split("\t")
        yield rating, 1

    def reducer(self, rating, counts):
        total = 0

        for count in counts:
            total += count

        yield rating, total

if __name__ == '__main__':
    MRRatingCounter.run()
