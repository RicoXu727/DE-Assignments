# The second python file contains all the functions needs
import random

global score
def initialize_grid():
    grid = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if not empty_cells:
        return
    i, j = random.choice(empty_cells)
    grid[i][j] = 2

# [2, 0, 4, 8] -> [2, 4, 8, 0]
def left_compress(grid):
    new_grid = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                pos += 1
    return new_grid
# [2, 0, 4, 4] -> [2, 8, 0, 0]
score = 0  # Global variable to keep track of the score

def left_merge(grid):
    global score 
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                merged_value = grid[i][j] * 2
                grid[i][j] = merged_value
                grid[i][j + 1] = 0
                score += merged_value 
    return grid


# [2, 0, 4, 2] -> [2, 4, 0, 2]
def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][3 - j])
    return new_grid

# transposed version of the grid
def transpose(grid):
    new_grid = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[j][i]
    return new_grid

def move_left(grid):
    grid = left_compress(grid)
    grid = left_merge(grid)
    grid = left_compress(grid)
    return grid

# left + reverse
def move_right(grid):
    grid = reverse(grid)
    grid = move_left(grid)
    grid = reverse(grid)
    return grid

# left + transpose
def move_up(grid):
    grid = transpose(grid)
    grid = move_left(grid)
    grid = transpose(grid)
    return grid

# right + transpose
def move_down(grid):
    grid = transpose(grid)
    grid = move_right(grid)
    grid = transpose(grid)
    return grid

def can_move(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return True
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return True
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return True
    return False

def find_max_number(grid):
    max_number = max(max(row) for row in grid)
    return max_number

def print_grid(grid):
    print('Score : ' + str(score))
    print()
    for i in range(4):
        print(' '.join(str(grid[i][j]).rjust(4) for j in range(4)))
        print()
