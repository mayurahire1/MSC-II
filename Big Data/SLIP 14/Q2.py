# 2. Consider a book txt file. Write a Map Reduce program to display word count in sorted order.

# Repeated - SLIP 14, 16

from mrjob.job import MRJob
from mrjob.step import MRStep


class MRWordCount(MRJob):

    def mapper(self, key, line):
        for word in line.split():
            word = word.lower().strip(".,!?;:")
            if word:
                yield word, 1

    def reducer(self, word, counts):
        total = sum(counts)
        yield None, (word, total)

    def reducer_sort(self, key, values):
        sorted_words = sorted(values)

        for word, count in sorted_words:
            yield word, count

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_sort)
        ]


if __name__ == '__main__':
    MRWordCount.run()