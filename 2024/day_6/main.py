file_number = 2
part_1 = True
from competitive import Point
# import numpy as np
with open(f'{file_number}.txt') as f:
    lab = f.read().rstrip().split('\n')
print(f"lab = {lab}")

height = len(lab)
width = len(lab[0])

initial_pos = pos = Point(0, 0)
for i in range(height):
    for j in range(width):
        if lab[i][j] == '^':
            pos.y = i
            pos.x = j
print(f"pos.y = {pos.y}")
print(f"pos.x = {pos.x}")

orientation = Point(-1, 0)

positions = set()
positions.add(pos)

import time

now = time.time()
while True:
    new_pos = pos + orientation
    if (new_pos.y < 0 or new_pos.y >= height or new_pos.x < 0 or new_pos.x >= width):
        break
    while lab[new_pos.y][new_pos.x] == "#":
        orientation.rotateClockwise90()
        new_pos = pos + orientation
    positions.add(new_pos)
    pos = new_pos

elapsed = time.time() - now

answer_1 = len(positions)
print(f"answer_1 = {answer_1}")

##


# part 2
answer_2 = 0


lab = [list(l) for l in lab]

for i in range(height):
    for j in range(width):
        print(f"i = {i}")
        print(f"j = {j}")
        if lab[i][j] in '#^':
            continue
        else:
            temp = lab[i][j]
            lab[i][j] = "#"

            positions = set()
            pos = initial_pos
            orientation = Point(-1, 0)
            positions.add((pos, orientation))
            has_cycle = True
            while True:
                new_pos = pos + orientation
                if (new_pos.y < 0 or new_pos.y >= height or new_pos.x < 0 or new_pos.x >= width):
                    has_cycle = False
                    break
                while lab[new_pos.y][new_pos.x] == "#":
                    orientation.rotateClockwise90()
                    new_pos = pos + orientation

                if (new_pos, orientation) in positions:
                    has_cycle = True
                    break
                positions.add((new_pos, orientation))
                pos = new_pos

            answer_2 += has_cycle
            lab[i][j] = temp
print(f"answer_2 = {answer_2}")
