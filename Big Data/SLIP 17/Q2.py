# Consider a Book text file. Write a Map Reduce program to find word which has occurred maximum number of times.

from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMaxWord(MRJob):

    def mapper(self, key, line):
        for word in line.split():
            word = word.lower().strip(".,!?;:")
            if word:
                yield word, 1

    def reducer(self, word, counts):
        total = sum(counts)
        yield None, (total, word)

    def reducer_max(self, key, values):
        max_count = 0
        max_word = ""

        for count, word in values:
            if count > max_count:
                max_count = count
                max_word = word

        yield max_word, max_count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_max)
        ]

if __name__ == '__main__':
    MRMaxWord.run()