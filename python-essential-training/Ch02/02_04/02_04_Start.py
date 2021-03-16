# Statistics Module
import statistics
import math

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(sorted(agesData))
print(statistics.mean(agesData))
# mode is the most frequent value
print(statistics.mode(agesData))
print(statistics.median(agesData))

print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData)))
