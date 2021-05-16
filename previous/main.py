import numpy as np

# Load sudokus
sudoku = np.load("data/very_easy_puzzle.npy")
print("very_easy_puzzle.npy has been loaded into the variable sudoku")
print(f"sudoku.shape: {sudoku.shape}, sudoku[0].shape: {sudoku[0].shape}, sudoku.dtype: {sudoku.dtype}")

# Load solutions for demonstration
solutions = np.load("data/very_easy_solution.npy")
print()



def sudoku_sovled(game):
    if np.sum(game) == 405:
        return True
    else:
        return False

def sudoku_solver(sudoku):
    backup = sudoku
    sol=sudoku_solve(sudoku)
    if np.array_equal(backup, sol) and not sudoku_sovled(sol):
        blank = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1]])
        return blank
    else:
        return sol


def sudoku_solve(sudoku):
    current_state = sudoku
    for y_pos in range(9):
        for x_pos in range(9):
            if current_state[y_pos][x_pos] == 0:
                for possible in range(1, 10):
                    if check_move(current_state, y_pos, x_pos, possible):
                        current_state[y_pos, x_pos] = possible
                        current_state = sudoku_solve(current_state)
                        if not sudoku_sovled(current_state):
                            current_state[y_pos, x_pos] = 0
                        else:
                            return current_state
                return current_state
    return current_state

def check_move(temp_state, y_pos, x_pos, possible):
    # check rows and cols
    for index in range(9):
        if (temp_state[y_pos][index] == possible) or (temp_state[index][x_pos] == possible):
            return False
    sub_cell_y = (y_pos // 3) * 3
    sub_cell_x = (x_pos // 3) * 3
    for y in range (sub_cell_y, sub_cell_y+3):
        for x in range(sub_cell_x, sub_cell_x + 3):
            if temp_state[y][x] == possible:
                return False
    return True


# YOUR CODE HERE
# raise NotImplementedError()

SKIP_TESTS = False


def main():
    import time
    difficulties = ['very_easy', 'easy', 'medium', 'hard']
    #difficulties = ['very_easy', 'easy', 'medium']
    #difficulties = ['hard']

    for difficulty in difficulties:
        print(f"Testing {difficulty} sudokus")

        sudokus = np.load(f"data/{difficulty}_puzzle.npy")
        solutions = np.load(f"data/{difficulty}_solution.npy")

        count = 0
        for i in range(len(sudokus)):
        #for i in [1]:
            sudoku = sudokus[i].copy()

            start_time = time.process_time()
            your_solution = sudoku_solver(sudoku)
            end_time = time.process_time()

            #print(f"This is your solution for {difficulty} sudoku number", i)
            #print(your_solution)
            #print(solutions[i])
            #print("Is your solution correct?")
            print(f"This is your solution for {difficulty} sudoku number", i)
            if np.array_equal(your_solution, solutions[i]):
                print ("correct")
                #print(f"Correct solution for {difficulty} sudoku number", i)
                count += 1
                print("This sudoku took", end_time - start_time, "seconds to solve.\n")
            else:

                print ("wrong")
                #print(your_solution - solutions[i])
                print("This sudoku took", end_time - start_time, "seconds to solve.\n")

        print(f"{count}/{len(sudokus)} {difficulty} sudokus correct")
        if count < len(sudokus):
            break


#if not SKIP_TESTS:
#    tests()

main()
