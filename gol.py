import numpy as np



class GameOfLife:

    def __init__(self, grid, size, n_gen):
        self.grid = grid
        self.size = size
        self.n_gen = n_gen
    

    def count_alive_neighbours(self, on_grid, size, i, j):
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
                if 0 <= x < size and 0 <= y < size)


    def next_generation(self, on_grid, size):
        next_grid = np.zeros(shape=(size, size))
        for (i, j) in [(i, j) for i in range(size) for j in range(size)]:
            alive_n = self.count_alive_neighbours(on_grid, size, i, j)
            
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
        o = self.next_generation(self.grid, self.size)
        steps.append(o)

        for _ in range(self.n_gen-1):
            o = self.next_generation(o, self.size)
            steps.append(o)
        
        return steps
