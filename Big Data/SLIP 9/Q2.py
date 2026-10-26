# 2. Considerthe Temperature Data set. Write a Map Reduce program to find minimum temperature for each weather station


from mrjob.job import MRJob

class MRMinTemperature(MRJob):
    def mapper(self, key, line):
        fields = line.split(",")

        if fields[2] == "TMIN":
            yield fields[0], int(fields[3])

    def reducer(self, station, temperatures):
        minimum = min(temperatures)
        yield station, minimum

if __name__ == '__main__':
    MRMinTemperature.run()
