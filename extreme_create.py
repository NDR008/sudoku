import numpy as np

extreme = []
extremes = []
a = []
s = []

# Evil - https://www.extremesudoku.info/ - 13th May Set
a.append([
    [0, 0, 6, 2, 0, 0, 0, 0, 3],
    [0, 4, 0, 0, 5, 0, 0, 8, 0],
    [9, 0, 0, 0, 0, 3, 4, 0, 0],
    [2, 0, 0, 0, 0, 1, 8, 0, 0],
    [0, 9, 0, 0, 3, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 0, 0, 0, 5],
    [0, 0, 7, 3, 0, 0, 0, 0, 8],
    [0, 8, 0, 0, 4, 0, 0, 9, 0],
    [5, 0, 0, 0, 0, 7, 2, 0, 0]
])
s.append([
    [8, 5, 6, 2, 1, 4, 9, 7, 3],
    [7, 4, 3, 9, 5, 6, 1, 8, 2],
    [9, 2, 1, 7, 8, 3, 4, 5, 6],
    [2, 3, 5, 4, 7, 1, 8, 6, 9],
    [6, 9, 8, 5, 3, 2, 7, 4, 1],
    [1, 7, 4, 6, 9, 8, 3, 2, 5],
    [4, 6, 7, 3, 2, 9, 5, 1, 8],
    [3, 8, 2, 1, 4, 5, 6, 9, 7],
    [5, 1, 9, 8, 6, 7, 2, 3, 4]
])

# Arto Inkala - https://www.sudokuwiki.org/sudoku.htm
a.append([
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
])
s.append([
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 2, 3, 7, 8, 9, 6],
    [3, 6, 9, 8, 4, 5, 7, 2, 1],
    [2, 8, 7, 1, 6, 9, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 3, 6, 8],
    [4, 3, 8, 5, 2, 6, 9, 1, 7],
    [7, 9, 6, 3, 1, 8, 4, 5, 2]
])

# Shinning Mirror - https://www.sudokuwiki.org/sudoku.htm
a.append([
    [0, 0, 0, 0, 0, 1, 0, 0, 2],
    [0, 0, 3, 0, 0, 0, 0, 4, 0],
    [0, 5, 0, 0, 6, 0, 7, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 7, 0],
    [0, 0, 7, 0, 0, 3, 8, 0, 0],
    [9, 0, 0, 0, 5, 0, 0, 0, 1],
    [0, 0, 6, 0, 8, 0, 2, 0, 0],
    [0, 4, 0, 6, 0, 0, 0, 0, 7],
    [2, 0, 0, 0, 0, 9, 0, 6, 0]
])
s.append([
    [8, 7, 9, 4, 3, 1, 6, 5, 2],
    [6, 2, 3, 5, 9, 7, 1, 4, 8],
    [1, 5, 4, 2, 6, 8, 7, 9, 3],
    [4, 3, 2, 8, 1, 6, 5, 7, 9],
    [5, 1, 7, 9, 4, 3, 8, 2, 6],
    [9, 6, 8, 7, 5, 2, 4, 3, 1],
    [7, 9, 6, 3, 8, 4, 2, 1, 5],
    [3, 4, 1, 6, 2, 5, 9, 8, 7],
    [2, 8, 5, 1, 7, 9, 3, 6, 4]
])

# Extreme - https://www.extremesudoku.info/ - 13th May Set
a.append([
    [3, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 5, 2, 0, 4, 3, 0, 0],
    [0, 7, 0, 0, 8, 0, 0, 1, 0],
    [0, 4, 0, 7, 0, 9, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 6, 0, 8, 0, 2, 0, 4, 0],
    [0, 8, 0, 0, 7, 0, 0, 9, 0],
    [0, 0, 6, 4, 0, 3, 8, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 4]
])

s.append([
    [3, 2, 8, 9, 1, 7, 4, 6, 5],
    [1, 9, 5, 2, 6, 4, 3, 7, 8],
    [6, 7, 4, 3, 8, 5, 9, 1, 2],
    [8, 4, 1, 7, 5, 9, 6, 2, 3],
    [7, 3, 2, 1, 4, 6, 5, 8, 9],
    [5, 6, 9, 8, 3, 2, 7, 4, 1],
    [4, 8, 3, 5, 7, 1, 2, 9, 6],
    [2, 1, 6, 4, 9, 3, 8, 5, 7],
    [9, 5, 7, 6, 2, 8, 1, 3, 4]
])

# https://liorsinai.github.io/coding/2020/07/27/sudoku-solver.html - A 17-clue
a.append([
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 3, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 1, 8],
    [0, 0, 0, 0, 8, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 3, 0, 0]
])

s.append([
    [2, 6, 4, 7, 1, 5, 8, 3, 9],
    [1, 3, 7, 8, 9, 2, 6, 4, 5],
    [5, 9, 8, 4, 3, 6, 2, 7, 1],
    [4, 2, 3, 1, 7, 8, 5, 9, 6],
    [8, 1, 6, 5, 4, 9, 7, 2, 3],
    [7, 5, 9, 6, 2, 3, 4, 1, 8],
    [3, 7, 5, 2, 8, 1, 9, 6, 4],
    [9, 8, 2, 3, 6, 4, 1, 5, 7],
    [6, 4, 1, 9, 5, 7, 3, 8, 2]
])

# hole from https://github.com/MarionBarbee/Sudoku_solver
a.append([[0, 0, 6, 7, 0, 3, 5, 0, 0],
          [0, 0, 0, 0, 4, 0, 0, 0, 0],
          [5, 0, 0, 0, 0, 0, 0, 0, 2],
          [9, 0, 0, 0, 0, 0, 0, 0, 7],
          [0, 3, 0, 0, 0, 0, 0, 4, 0],
          [8, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 4],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 5, 9, 2, 6, 7, 3, 1, 0]])

s.append([
    [2, 4, 6, 7, 1, 3, 5, 8, 9],
    [7, 9, 8, 5, 4, 2, 1, 6, 3],
    [5, 1, 3, 6, 8, 9, 4, 7, 2],
    [9, 2, 4, 1, 5, 6, 8, 3, 7],
    [6, 3, 1, 9, 7, 8, 2, 4, 5],
    [8, 7, 5, 3, 2, 4, 6, 9, 1],
    [1, 6, 7, 8, 3, 5, 9, 2, 4],
    [3, 8, 2, 4, 9, 1, 7, 5, 6],
    [4, 5, 9, 2, 6, 7, 3, 1, 8]])

# killer application from https://github.com/MarionBarbee/Sudoku_solver
a.append([
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 6, 0, 0, 1, 0, 0, 0, 4],
    [0, 0, 3, 4, 0, 0, 2, 0, 0],
    [8, 0, 0, 0, 0, 3, 0, 5, 0],
    [0, 0, 2, 9, 0, 0, 7, 0, 0],
    [0, 4, 0, 0, 8, 0, 0, 0, 9],
    [0, 2, 0, 0, 6, 0, 0, 0, 7],
    [0, 0, 0, 1, 0, 0, 9, 0, 0],
    [7, 0, 0, 0, 0, 8, 0, 6, 0]
])

s.append([
    [9, 5, 4, 8, 2, 6, 1, 7, 3],
    [2, 6, 8, 3, 1, 7, 5, 9, 4],
    [1, 7, 3, 4, 9, 5, 2, 8, 6],
    [8, 1, 9, 7, 4, 3, 6, 5, 2],
    [6, 3, 2, 9, 5, 1, 7, 4, 8],
    [5, 4, 7, 6, 8, 2, 3, 1, 9],
    [4, 2, 1, 5, 6, 9, 8, 3, 7],
    [3, 8, 6, 1, 7, 4, 9, 2, 5],
    [7, 9, 5, 2, 3, 8, 4, 6, 1]
])

# intentional doubles
a.append([
    [1, 1, 6, 2, 0, 0, 0, 0, 3],
    [0, 4, 0, 0, 5, 0, 0, 8, 0],
    [9, 0, 0, 0, 0, 3, 4, 0, 0],
    [2, 0, 0, 0, 0, 1, 8, 0, 0],
    [0, 9, 0, 0, 3, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 0, 0, 0, 5],
    [0, 0, 7, 3, 0, 0, 0, 0, 8],
    [0, 8, 0, 0, 4, 0, 0, 9, 0],
    [5, 0, 0, 0, 0, 7, 2, 0, 0]
])
s.append([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

# very blank
a.append([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
])
s.append([[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [4, 5, 6, 7, 8, 9, 1, 2, 3],
          [7, 8, 9, 1, 2, 3, 4, 5, 6],
          [3, 1, 4, 2, 6, 5, 8, 9, 7],
          [2, 6, 5, 8, 9, 7, 3, 1, 4],
          [8, 9, 7, 3, 1, 4, 2, 6, 5],
          [5, 3, 1, 6, 4, 2, 9, 7, 8],
          [6, 4, 8, 9, 7, 1, 5, 3, 2],
          [9, 7, 2, 5, 3, 8, 6, 4, 1]])

# https://liorsinai.github.io/coding/2020/07/27/sudoku-solver.html
a.append([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0, 0],
    [0, 0, 0, 3, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
])

s.append([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

# https://liorsinai.github.io/coding/2020/07/27/sudoku-solver.html
a.append([
    [0, 0, 0, 0, 0, 5, 0, 8, 0],
    [0, 0, 0, 6, 0, 1, 0, 4, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 6, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 5],
    [5, 3, 0, 0, 0, 0, 0, 6, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
])

s.append([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]])

for i in range(len(a)):
    extreme.append(np.array(a[i]))
    extremes.append(np.array(s[i]))

print(len(a))
print(len(s))

np.save("data\extreme_puzzle.npy", extreme)
np.save("data\extreme_solution.npy", extremes)
