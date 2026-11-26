# # 2. Consider the Friends Data set. Write a Map Reduce program to find agewise number of friends sorted on age.


from mrjob.job import MRJob
from mrjob.step import MRStep

class MRFriends(MRJob):

    def mapper(self, key, line):
        (userID, name, age, friends) = line.split(",")
        yield int(age), 1

    def reducer(self, age, counts):
        total = sum(counts)
        yield None, (age, total)

    def reducer_sort(self, key, values):
        sorted_ages = sorted(values)

        for age, total in sorted_ages:
            yield age, total

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_sort)
        ]

if __name__ == '__main__':
    MRFriends.run()