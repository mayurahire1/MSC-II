# Consider the Friends data set. Write a MapReduce program to find the person having maximun number of friends.

from mrjob.job import MRJob

class MRMaxFriends(MRJob):

    def mapper(self, key, line):
        (userID, name, age, friends) = line.split(",")
        yield None, (int(friends), name)

    def reducer(self, key, values):
        max_friends = 0
        max_name = ""

        for friends, name in values:
            if friends > max_friends:
                max_friends = friends
                max_name = name

        yield max_name, max_friends

if __name__ == '__main__':
    MRMaxFriends.run()