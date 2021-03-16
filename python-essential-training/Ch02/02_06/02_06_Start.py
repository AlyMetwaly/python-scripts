# Itertools Part 2
import itertools
# Permutations: Order matters - some copies with same inputs but in different order
election = {1: "Barb", 2: "Karen", 3: "Erin"}
binary = [0, 1, 2]
for p in itertools.permutations(election):
    print(p)
for p1 in itertools.permutations(election.values()):
    print(p1)

# Combinations: Order does not matter - no copies with same inputs
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in itertools.combinations(colorsForPainting, 1):
    print(c)
for c in itertools.combinations(binary, 2):
    print(c)
