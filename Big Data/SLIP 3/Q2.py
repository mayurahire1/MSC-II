# Consider the Movie Data set. Write a Map Reduce program to find number of movies watched by each user.


from mrjob.job import MRJob

class MRMoviesPerUser(MRJob):
    def mapper(self, key, line):
        (userID, movieID, rating, timestamp) = line.split("\t")
        yield userID, 1

    def reducer(self, userID, counts):
        total = 0

        for count in counts:
            total += count

        yield userID, total

if __name__ == '__main__':
    MRMoviesPerUser.run()
