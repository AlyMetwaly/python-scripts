# Least to Greatest
points_in_game = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(points_in_game)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda", "Aly"]
print(sorted(children))
print(sorted(children, reverse=True))
# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(points_in_game, reverse=True))

leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
print(leaderBoard[432])
print(leaderBoard.get(432))

students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
print(sorted(students, key=lambda student: student[0]))
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[2]))
