# 2. Consider the Friends Data set. Write a Map Reduce program to find average number friends for each age value.


from mrjob.job import MRJob

class MRAverageFriends(MRJob):
    def mapper(self, key, line):
        (userID, name, age, friends) = line.split(",")

        yield age, (int(friends), 1)

    def reducer(self, age, values):
        total = 0
        count = 0

        for friends, people in values:
            total += friends
            count += people

        average = total / count
        yield age, average

if __name__ == '__main__':
    MRAverageFriends.run()