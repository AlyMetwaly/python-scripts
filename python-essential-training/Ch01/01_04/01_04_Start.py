# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple (It enumerates the range and turns it into iterable tuple)

numberedContestants = range(30)
print(type(numberedContestants))
print(list(numberedContestants))

for c in numberedContestants:
    print("Contestant " + str(c) + " is here")

luckyWinners = range(7, 30, 5)
print(list(luckyWinners))
