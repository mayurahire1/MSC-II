# Repeated - SLIP 1, 8, 12, 13

# 2. Consider the Movie Data set. Write a Map Reduce program to find average rating per user.


from mrjob.job import MRJob

class MRRatingCounter(MRJob):
    def mapper(self, key, line):
        (userID, movieID, rating, timestamp) = line.split("\t")
        yield userID, float(rating)

    def reducer(self, userID, ratings):
        total = 0
        count = 0

        for rating in ratings:
            total += rating
            count += 1

        average = total / count
        yield userID, average

if __name__ == '__main__':
    MRRatingCounter.run()