file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

from itertools import product
from collections import deque
from typing import DefaultDict

height = len(entries)
width = len(entries[0])
answer_1 = 0
answer_2 = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

seen = set()
for r, c in product(range(height), range(width)):
    area = 0
    q = deque([(r, c)])
    perimeter_number = 0
    perimeter = DefaultDict(set)
    letter = entries[r][c]
    while q:
        row, column = q.popleft()
        if (row, column) in seen:
            continue;
        seen.add((row, column))
        area += 1
        for dir_row, dir_column in directions:
            new_row = row + dir_row
            new_column = column + dir_column
            # print(f"new_row = {new_row}")
            # print(f"new_column = {new_column}")
            if 0 <= new_row < height and 0 <= new_column < width and letter == entries[new_row][new_column]:
                # print("hello world")
                q.append((new_row, new_column))
            else:
                perimeter_number += 1
                perimeter[(dir_row, dir_column)].add((new_row, new_column))
    
    answer_1 += perimeter_number * area
    
    sides = 0
    for direction in perimeter.keys():
        seen_perimeters = set()
        for row, column in perimeter[direction]:
            if (row, column) in seen_perimeters:
                continue;
            sides += 1
            q = deque([(row, column)])
            while q:
                row, column = q.popleft()
                if (row, column) in seen_perimeters:
                    continue;
                seen_perimeters.add((row, column))
                for dir_row, dir_column in directions:
                    new_row = row + dir_row
                    new_column = column + dir_column
                    if (new_row, new_column) in perimeter[direction]:
                        q.append((new_row, new_column))

    answer_2 += sides * area

answer_1
answer_2
