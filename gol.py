import numpy as np



class GameOfLife:

    def __init__(self, grid, n_gen):
        self.grid = grid
        self.n_gen = n_gen
        self.size_y = len(grid)
        self.size_x = len(grid[0])

        self.rules = [
            [0,0,0,1,0,0,0,0,0,0],
            [0,0,1,1,0,0,0,0,0,0],
        ]
    

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

        return sum(on_grid[x][y] for x, y in neighbors
                if 0 <= x < self.size_x and 0 <= y < self.size_y)


    def next_generation(self, on_grid):
        next_grid = np.zeros(shape=(self.size_y, self.size_x))
        for (i, j) in [(i, j) for i in range(self.size_y) for j in range(self.size_x)]:
            cell_status = int(on_grid[i, j])
            alive_n = int(self.count_alive_neighbours(on_grid, i, j))
            next_grid[i,j] = self.rules[cell_status][alive_n]
        return next_grid


    def generate_steps(self):
        steps = []
        step = self.grid
        steps.append(step)
        for _ in range(self.n_gen):
            step = self.next_generation(step)
            steps.append(step)
        
        return steps
