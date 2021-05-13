import numpy as np

# a way of checking if we completed the grid (assuming all rules followed)
def sudoku_sovled(sudoku):
    if np.sum(sudoku) == 405 and len(sudoku_zeros(sudoku))==0:
        return True
    else:
        return False


# find all zeros
def sudoku_zeros2(sudoku):
    zeros_index = []
    for y_pos in range(9):
        for x_pos in range(9):
            if sudoku[y_pos][x_pos] == 0:
                zeros_index.append((y_pos, x_pos))
    return zeros_index

def sudoku_zeros(sudoku):
    zeros_index = [(y_pos, x_pos) for y_pos in range(9) for x_pos in range(9) if sudoku[y_pos][x_pos] == 0]
    return zeros_index


def naked_singles(sudoku):
    valid_options = possibilities(sudoku)
    for k in valid_options:
        if len(valid_options[k]) == 1:
            sudoku[k] = valid_options[k][0]
    return sudoku

def naked_pairs(sudoku):
    valid_options = possibilities_pairs(sudoku)
    for k in valid_options:
        if len(valid_options[k]) == 1:
            sudoku[k] = valid_options[k][0]
    return sudoku

def naked_helper(a,b):
    z = []
    for value in a:
        if value not in b:
            z.append(value)

    return z
    #return list(np.setdiff1d(a, b)) #slower since we need a list


def hidden_singles(sudoku):
    zeros = sudoku_zeros(sudoku)
    valid_options = possibilities(sudoku)
    for (y_pos, x_pos) in zeros:
        option = valid_options[(y_pos, x_pos)]
        for col in range(9):
            if col == x_pos:
                continue
            elif (y_pos, col) in valid_options:
                d = valid_options[(y_pos, col)]
                option = naked_helper(option, d)
            if len(option) < 1:
                break
        if len(option) == 1:
            # it could be this value will violates other cells (like hard 15)
            if check_move(sudoku, y_pos, x_pos, option[0]):
                sudoku[(y_pos, x_pos)] = option[0]
            else:
                return -1 * np.ones_like(sudoku)

    zeros = sudoku_zeros(sudoku)
    valid_options = possibilities(sudoku)
    for (y_pos, x_pos) in zeros:
        option = valid_options[(y_pos, x_pos)]
        for row in range(9):
            if row == y_pos:
                continue
            elif (row, x_pos) in valid_options:
                d = valid_options[(row, x_pos)]
                option = naked_helper(option, d)
        if len(option) == 1:
            # it could be this value will violates other cells (like hard 15)
            if check_move(sudoku, y_pos, x_pos, option[0]):
                sudoku[(y_pos, x_pos)] = option[0]
            else:
                return -1 * np.ones_like(sudoku)

    zeros = sudoku_zeros(sudoku)
    valid_options = possibilities(sudoku)
    for (y_pos, x_pos) in zeros:
        option = valid_options[(y_pos, x_pos)]
        sub_cell_y = (y_pos // 3) * 3
        sub_cell_x = (x_pos // 3) * 3
        for y in range(sub_cell_y, sub_cell_y + 3):
            for x in range(sub_cell_x, sub_cell_x + 3):
                if x == x_pos and y == y_pos:
                    continue
                elif (y, x) in valid_options:
                    d = valid_options[(y, x)]
                    option=naked_helper(option, d)
        if len(option) == 1:
            if check_move(sudoku, y_pos, x_pos, option[0]):
                sudoku[(y_pos, x_pos)] = option[0]
            else:
                return -1 * np.ones_like(sudoku)
    return sudoku

def possibilities(sudoku):
    zeros = sudoku_zeros(sudoku)
    valid_options = {}
    for (y_pos, x_pos) in zeros:
            tmp = []
            for possible in range(1, 10):
                if check_move(sudoku, y_pos, x_pos, possible):
                    tmp.append(possible)
            valid_options[(y_pos, x_pos)] = tmp
    return valid_options


def possibilities_pairs(sudoku):
    valid_options = possibilities(sudoku)
    for row in range(9):
        for col in range(9):
            if (row, col) in valid_options:
                val = valid_options[row, col]
                if len(val) == 2:
                    for col1 in range(9):
                        if (row, col1) in valid_options:
                            val1 = valid_options[row, col1]
                            if col1 != col and len(val1) == 2 and val == val1:
                                for col2 in range(9):
                                    if (row, col2) in valid_options:
                                        if col2 != col and col2 != col1:
                                            val2 = valid_options[(row, col2)]
                                            valid_options[(row, col2)] = naked_helper(val2, val)

    for col in range(9):
        for row in range(9):
            if (row, col) in valid_options:
                val = valid_options[row, col]
                if len(val) == 2:
                    for row1 in range(9):
                        if (row1, col) in valid_options:
                            val1 = valid_options[row1, col]
                            if row1 != row and len(val1) == 2 and val == val1:
                                for row2 in range(9):
                                    if (row2, col) in valid_options:
                                        if row2 != row and row2 != row1:
                                            val2 = valid_options[(row2, col)]
                                            valid_options[(row2, col)] = naked_helper(val2, val)

        for row in [0,3,6]:
            for col in [0,3,6]:
                suby = (row // 3) * 3
                subx = (col // 3) * 3
                for y in range(suby, suby + 3):
                    for x in range(subx, subx + 3):
                        if (y,x) in valid_options:
                            val = valid_options[y, x]
                            if len(val) == 2:
                                for y1 in range(suby, suby + 3):
                                    for x1 in range(subx, subx + 3):
                                        if (y1, x1) in valid_options:
                                            val1 = valid_options[y1, x1]
                                            if (y1,x1) != (y,x) and len(val1) == 2 and val == val1:
                                                for y2 in range(suby, suby + 3):
                                                    for x2 in range(subx, subx + 3):
                                                        if (y2, x2) in valid_options:
                                                            if (y2,x2) != (y,x) and (y2,x2) != (y1,x1):
                                                                val2 = valid_options[(y2, x2)]
                                                                valid_options[(y2, x2)] = naked_helper(val2, val)
    return valid_options


def sudoku_solver(sudoku):
    loop_flag = True
    sudoku = naked_pairs(sudoku)
    while loop_flag:
        start = sudoku.copy()
        sudoku = hidden_singles(sudoku)
        sudoku = naked_pairs(sudoku)
        finish = sudoku.copy()
        if np.array_equal(start, finish):
            loop_flag = False
    if np.sum(sudoku) < 0:
        return sudoku
    elif sudoku_sovled(sudoku):
        return sudoku
    valid_options = sort_by_values_len(possibilities_pairs(sudoku))
    zeros = sudoku_zeros(sudoku)
    sudoku = sudoku_solve(valid_options, zeros, sudoku)
    if not sudoku_sovled(sudoku):
        return -1 * np.ones_like(sudoku)
    else:
        return sudoku


def sudoku_solve(valid_options, zeros, current_state):
    for (y_pos, x_pos) in zeros:
        valid_values = valid_options[(y_pos, x_pos)]
        for possible in valid_values:
            if check_move(current_state, y_pos, x_pos, possible):
                current_state[y_pos, x_pos] = possible
                dump, *new_zeros = zeros
                current_state = sudoku_solve(valid_options, new_zeros, current_state)
                if not sudoku_sovled(current_state):
                    current_state[y_pos, x_pos] = 0
                else:
                    break
        break
    return current_state


def check_move(temp_state, y_pos, x_pos, possible):
    for index in range(9):
        if (temp_state[y_pos][index] == possible) or (temp_state[index][x_pos] == possible):
            return False
    sub_cell_y = (y_pos // 3) * 3
    sub_cell_x = (x_pos // 3) * 3
    for y in range(sub_cell_y, sub_cell_y + 3):
        for x in range(sub_cell_x, sub_cell_x + 3):
            if temp_state[y][x] == possible:
                return False
    return True


def sort_by_values_len(d):
    z = {}
    for k in sorted(d, key=lambda k: len(d[k])):
        z[k] = d[k]
    return z

SKIP_TESTS = False


def main():
    import time
    difficulties = ['very_easy', 'easy', 'medium', 'hard', 'extreme']
    difficulties = ['hard']

    for difficulty in difficulties:
        print(f"Testing {difficulty} sudokus")

        sudokus = np.load(f"data/{difficulty}_puzzle.npy")
        solutions = np.load(f"data/{difficulty}_solution.npy")

        count = 0
        main_start_time = time.process_time()
        for i in range(len(sudokus)):
        #for i in [10]:

            for j in range(1):
                sudoku = sudokus[i].copy()
                a = sort_by_values_len(possibilities(sudoku))
                #print(sudoku)
                start_time = time.process_time()
                your_solution = sudoku_solver(sudoku)
                end_time = time.process_time()


                if np.array_equal(your_solution, solutions[i]):
                    #print(f"[OK] Test {difficulty}", i, "This sudoku took", end_time - start_time, "seconds to solve.")
                    print(i, end_time - start_time)
                    #print(np.sum(solutions[i]))
                    count += 1
                else:
                    print(f"[[NG]] Test {difficulty}", i, "This sudoku took", end_time - start_time, "seconds to solve.")


        if count != len(sudokus):
            print("SHIIIIIIIIIIIIIIIIIIIIIIIIIIIIITTTTTTTTT")
            # if count < len(sudokus):
            #    break
        main_end_time = time.process_time()
        print("total run time :", main_end_time-main_start_time)
main()