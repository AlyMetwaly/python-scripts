# Itertools
import itertools
# Infinite Counting
for x in itertools.count(50, 5):
    print(x)
    if x > 80:
        break
# Infinite Cycling
x = 0
for c in itertools.cycle([1, 2, 3, 4]):
    print(c)
    x = x+1
    if x > 50:
        break
# Infinite Repeating
for r in itertools.repeat([1, 2, 3]):
    print(r)
    x = x+1
    if x > 100:
        break
