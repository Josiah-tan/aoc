file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

entries = [list(map(lambda x: int(x) if x != '.' else '.', entry)) for entry in entries]

height = len(entries)
width = len(entries[0])

from queue import Queue

part_1 = 0
part_2 = 0
for i in range(height):
    for j in range(width):
        if entries[i][j] == 0:
            q = Queue()
            q.put((i, j))
            seen = set()
            while not q.empty():
                (y, x) = q.get()
                if entries[y][x] == 9:
                    seen.add((y, x))
                    part_2 += 1
                    continue;
                dir_y, dir_x = 1, 0
                for _ in range(4):
                    new_y = y + dir_y
                    new_x = x + dir_x
                    if 0 <= new_y < height and 0 <= new_x < width and entries[y][x] != '.' and entries[new_y][new_x] != '.':
                        if entries[y][x] == entries[new_y][new_x] - 1:
                            q.put((new_y, new_x))
                    dir_y, dir_x = -dir_x, dir_y
            part_1 += len(seen)
print(f"part_1 = {part_1}")
print(f"part_2 = {part_2}")
