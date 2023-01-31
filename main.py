import numpy as np
import urwid

from gol import GameOfLife

def unhandled_input(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

def refresh(_loop, _data):
    outputTxt = pretty_print(steps[_data % len(steps)])

    txt.set_text(outputTxt)
    _data += 1
    loop.set_alarm_in(1, refresh, _data)

def draw_fpentamino(on_grid):
    on_grid[4, 4] = 1
    on_grid[4, 5] = 1
    on_grid[5, 3] = 1
    on_grid[5, 4] = 1
    on_grid[6, 4] = 1

def draw_blinker(on_grid):
    on_grid[4, 4] = 1
    on_grid[4, 5] = 1
    on_grid[4, 6] = 1

def draw_semaphore(on_grid):
    on_grid[5, 4] = 1
    on_grid[5, 5] = 1
    on_grid[5, 6] = 1
    on_grid[4, 5] = 1

def draw_glider(on_grid):
    on_grid[3, 1] = 1
    on_grid[3, 2] = 1
    on_grid[3, 3] = 1
    on_grid[2, 3] = 1
    on_grid[1, 2] = 1

def pretty_print(step):
    return "\n".join(["".join(str(x)) for x in step]).replace('0',' ').replace('1','#')

size= 11
n_gen = 50
grid = np.zeros(shape=(size,size))

draw_glider(grid)


gol = GameOfLife(grid, n_gen)
steps = gol.generate_steps()

frame = 0
output_text = pretty_print(steps[frame])
txt = urwid.Text(output_text)
fill = urwid.Filler(txt, 'top')

loop = urwid.MainLoop(fill, unhandled_input=unhandled_input)
frame += 1
loop.set_alarm_in(2, refresh, frame)
loop.run()
