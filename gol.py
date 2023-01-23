import numpy as np



class GameOfLife:

    def __init__(self, grid, n_gen):
        self.grid = grid
        self.n_gen = n_gen
        self.size_y = len(grid)
        self.size_x = len(grid[0])
    

    def count_alive_neighbours(self, on_grid, i, j):
        neighbors = [
            (i-1, j),   # n
            (i-1, j-1), # nw
            (i, j-1),   # w
            (i+1, j-1), # sw
            (i+1, j),   # s
            (i+1, j+1), # se
            (i, j+1),   # e
            (i-1, j+1)  # ne
            ]

        return sum(on_grid[x][y] == 1 for x, y in neighbors
                if 0 <= x < self.size_x and 0 <= y < self.size_y)


    def next_generation(self, on_grid):
        next_grid = np.zeros(shape=(self.size_y, self.size_x))
        for (i, j) in [(i, j) for i in range(self.size_y) for j in range(self.size_x)]:
            alive_n = self.count_alive_neighbours(on_grid, i, j)
            
            cur_cell = on_grid[i, j]
            if cur_cell == 1:
                if alive_n < 2:
                    next_grid[i, j] = 0
                if alive_n > 3:
                    next_grid[i, j] = 0
                if alive_n ==  2 or alive_n == 3:
                    next_grid[i, j] = 1
            else:
                if cur_cell == 0:
                    if alive_n == 3:
                        # current cell come alive
                        next_grid[i, j] = 1
                else:
                    next_grid[i, j] = 0
        return next_grid


    def generate_steps(self):
        steps = []
        steps.append(self.grid)
        o = self.next_generation(self.grid)
        steps.append(o)

        for _ in range(self.n_gen-1):
            o = self.next_generation(o)
            steps.append(o)
        
        return steps
