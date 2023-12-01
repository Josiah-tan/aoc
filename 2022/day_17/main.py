import numpy as np
file_number = 2
part_1 = True
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    pattern = f.read().rstrip().split('\n')[0]
    # print(f"pattern = {pattern}")

def patternGenerator(pattern):
    while True:
        for character in pattern:
            yield character

blocks = [
(np.array([['#'] * 4])),
(np.array([
    ['.', '#', '.'],
    ['#', '#', '#'],
    ['.', '#', '.']
    ])),
(np.array([
    ['.', '.', '#'],
    ['.', '.', '#'],
    ['#', '#', '#']
    ])),
(np.array([4 * ['#']]).reshape((4, 1))),
(np.array([4 * ['#']]).reshape((2, 2)))
]
# print(f"blocks = {blocks}")

def blockGenerator(blocks, number):
    for i in range(number):
        yield blocks[i % len(blocks)]

grid = np.array([['.'] * 7] * 2020 * 4)
# grid.shape


def check(x, y, block):
    if x < 0 or x + block.shape[1] == grid.shape[1] + 1:
        return False;
    if y + block.shape[0] == grid.shape[0] + 1:
        return False;
    for i in range(block.shape[0]):
        grid_y = y + i
        for j in range(block.shape[1]):
            grid_x = x + j
            if grid[grid_y][grid_x] == '#' and block[i][j] == '#':
                return False;
    return True;

def draw(x, y, block):
    for i in range(block.shape[0]):
        grid_y = y + i
        for j in range(block.shape[1]):
            grid_x = x + j
            if block[i][j] == "#":
                grid[grid_y][grid_x] = "#"

tallest = grid.shape[0]
infinite_pattern = patternGenerator(pattern)

for block in blockGenerator(blocks, 2022):
    x = 2
    y = tallest - 3 - block.shape[0]
    while True:
        next_pattern = next(infinite_pattern)
        direction = 1 if next_pattern == '>' else -1
        if check(x + direction, y, block):
            x += direction
        if check(x, y + 1, block):
            y += 1
        else:
            tallest = min(tallest, y)
            height = grid.shape[0] - tallest
            break;
    draw(x, y, block)

        
# print(f"grid[-5:] = \n{grid[-20:]}")
height = grid.shape[0] - tallest
print(f"height = {height}") 
