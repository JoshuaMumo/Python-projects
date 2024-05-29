#2048 game
import random
import os
def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    add_new_tile(grid)
    return grid
def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])
def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("2048 GAME")
    print("---------------------")
    for row in grid:
        print('|'.join(str(cell).center(5) if cell != 0 else ' ' * 5 for cell in row))
        print("---------------------")
def move_left(grid):
    for i in range(4):
        merged = False
        for j in range(1, 4):
            if grid[i][j] != 0:
                k = j
                while k > 0 and grid[i][k - 1] == 0:
                    grid[i][k - 1] = grid[i][k]
                    grid[i][k] = 0
                    k -= 1
                if k > 0 and grid[i][k - 1] == grid[i][k] and not merged:
                    grid[i][k - 1] *= 2
                    grid[i][k] = 0
                    merged = True
def move_right(grid):
    for i in range(4):
        merged = False
        for j in range(2, -1, -1):
            if grid[i][j] != 0:
                k = j
                while k < 3 and grid[i][k + 1] == 0:
                    grid[i][k + 1] = grid[i][k]
                    grid[i][k] = 0
                    k += 1
                if k < 3 and grid[i][k + 1] == grid[i][k] and not merged:
                    grid[i][k + 1] *= 2
                    grid[i][k] = 0
                    merged = True
def move_up(grid):
    for j in range(4):
        merged = False
        for i in range(1, 4):
            if grid[i][j] != 0:
                k = i
                while k > 0 and grid[k - 1][j] == 0:
                    grid[k - 1][j] = grid[k][j]
                    grid[k][j] = 0
                    k -= 1
                if k > 0 and grid[k - 1][j] == grid[k][j] and not merged:
                    grid[k - 1][j] *= 2
                    grid[k][j] = 0
                    merged = True
def move_down(grid):
    for j in range(4):
        merged = False
        for i in range(2, -1, -1):
            if grid[i][j] != 0:
                k = i
                while k < 3 and grid[k + 1][j] == 0:
                    grid[k + 1][j] = grid[k][j]
                    grid[k][j] = 0
                    k += 1
                if k < 3 and grid[k + 1][j] == grid[k][j] and not merged:
                    grid[k + 1][j] *= 2
                    grid[k][j] = 0
                    merged = True
def is_game_over(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
    return True
def main():
    grid = initialize_grid()
    display_grid(grid)
    while not is_game_over(grid):
        move = input("Enter move (W or A or S or D): ")
        if move == 'W' or 'w':
            move_up(grid)
        elif move == 'A' or 'a':
            move_left(grid)
        elif move == 'S' or 's':
            move_down(grid)
        elif move == 'D' or 'd':
            move_right(grid)
        else:
            print("Invalid move! Use (W or A or S or D.)")
            continue
        add_new_tile(grid)
        display_grid(grid)
    print("Game Over!")

if __name__ == "__main__":
    main()