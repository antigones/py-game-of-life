import numpy as np
import urwid


class GameOfLife:

    def __init__(self, grid, size, n_gen):
        self.grid = grid
        self.size = size
        self.n_gen = n_gen
    
    def count_alive_neighbours(self, on_grid: np.ndarray, size:int, i:int, j:int):
        neighbors = [
            (i-1,j), #n
            (i-1,j-1), # nw
            (i,j-1), # w
            (i+1,j-1),# sw
            (i+1,j), # s
            (i+1,j+1),# se
            (i,j+1), # e
            (i-1,j+1) # ne
            ]

        return sum(on_grid[x][y] == 1 for x, y in neighbors
                if 0 <= x < size and 0 <= y < size)



    def next_generation(self, on_grid:np.ndarray, size:int):
        next_grid = np.zeros(shape=(size,size))
        for (i,j) in [(i,j) for i in range(size) for j in range(size)]:
            alive_n = self.count_alive_neighbours(on_grid,size,i,j)
            
            cur_cell = on_grid[i,j]
            if cur_cell == 1:
                if alive_n < 2:
                    next_grid[i,j] = 0
                if alive_n > 3:
                    next_grid[i,j] = 0
                if alive_n ==  2 or alive_n == 3:
                    next_grid[i,j] = 1
            else:
                if cur_cell == 0:
                    if alive_n == 3:
                        # current cell come alive
                        next_grid[i,j] = 1
                else:
                    next_grid[i,j] = 0
        return next_grid


    def generate_steps(self):
        steps = []
        steps.append(self.grid)
        o = self.next_generation(self.grid,self.size)
        steps.append(o)

        for _ in range(self.n_gen-1):
            o = self.next_generation(o,self.size)
            steps.append(o)
        
        return steps


def unhandled_input(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

def refresh(_loop, _data):
    outputTxt = pretty_print(steps[_data % len(steps)])

    txt.set_text(outputTxt)
    _data += 1
    loop.set_alarm_in(0.5, refresh, _data)

def draw_fpentamino(on_grid: np.ndarray):
    on_grid[4,4] = 1
    on_grid[4,5] = 1
    on_grid[5,3] = 1
    on_grid[5,4] = 1
    on_grid[6,4] = 1

def draw_blinker(on_grid: np.ndarray):
    on_grid[4,4] = 1
    on_grid[4,5] = 1
    on_grid[4,6] = 1

def draw_glider(on_grid: np.ndarray):
    on_grid[5,4] = 1
    on_grid[5,5] = 1
    on_grid[5,6] = 1
    on_grid[4,5] = 1

def pretty_print(step):
    a = "\n".join(["".join(str(x)) for x in step]).replace('0',' ').replace('1','#')
    return a

size= 11
n_gen = 9
grid = np.zeros(shape=(size,size))

draw_glider(grid)


gol = GameOfLife(grid, size, n_gen)
steps = gol.generate_steps()

frame = 0
output_text = pretty_print(steps[frame])
txt = urwid.Text(output_text)
fill = urwid.Filler(txt, 'top')

loop = urwid.MainLoop(fill, unhandled_input=unhandled_input)
frame += 1
loop.set_alarm_in(2, refresh, frame)
loop.run()
