# 2. Consider a Book text file. Write a Map Reduce program to find word count.


from mrjob.job import MRJob

class MRWordCount(MRJob):
    def mapper(self, key, line):
        for word in line.split():
            word = word.lower().strip(".,!?;:")
            if word:
                yield word, 1

    def reducer(self, word, counts):
        total = 0

        for count in counts:
            total += count

        yield word, total

if __name__ == '__main__':
    MRWordCount.run()
