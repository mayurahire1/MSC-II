# 2. Considerthe Temperature Data set. Write a Map Reduce program to find maximum temperature for each weather station.


from mrjob.job import MRJob

class MRMaxTemperature(MRJob):
    def mapper(self, key, line):
        fields = line.split(",")

        if fields[2] == "TMAX":
            yield fields[0], int(fields[3])

    def reducer(self, station, temperatures):
        maximum = max(temperatures)
        yield station, maximum

if __name__ == '__main__':
    MRMaxTemperature.run()
