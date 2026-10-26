# 2. Consider the Friends Data set. Write a Map Reduce program to find agewise number of friends sorted on age.


from mrjob.job import MRJob

class MRFriendsByAge(MRJob):
    def mapper(self, key, line):
        (userID, name, age, friends) = line.split(",")
        
        yield int(age), int(friends)

    def reducer(self, age, friends_values):
        total = 0

        for friends in friends_values:
            total += friends

        yield age, total

if __name__ == '__main__':
    MRFriendsByAge.run()
