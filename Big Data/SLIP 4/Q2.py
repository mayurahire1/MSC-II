# Consider the Friends Data set. Write a Map Reduce program to find number of friends per user.


from mrjob.job import MRJob

class MRFriendsCounter(MRJob):
    def mapper(self, key, line):
        (userID, name, age, friends) = line.split(",")

        if userID.isdigit():
            yield userID, int(friends)

    def reducer(self, userID, friends_values):
        total = 0

        for friends in friends_values:
            total += friends

        yield userID, total

if __name__ == '__main__':
    MRFriendsCounter.run()