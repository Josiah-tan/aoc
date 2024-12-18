file_number = 2
part_1 = True
from collections import deque
from typing import DefaultDict
from competitive import Point, sign, showMap
import sys
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

if file_number == 1:
    number_bytes = 12
    size = 7
else:
    number_bytes = 1024
    size = 71


len(entries)

mapping = [["."] * size for _ in range(size)]


showMap(mapping)


for byte_number in range(len(entries)):
    print(byte_number)
    x, y = map(int,entries[byte_number].split(","))
    mapping[y][x] = "#"
        


    distance = DefaultDict(lambda: sys.maxsize)
    q = deque([(0, 0)])

    current_distance = 0
    while q:
        for item_index in range(len(q)):
            i, j = q.popleft()
            if distance[(i, j)] != sys.maxsize:
                continue;
            distance[(i, j)] = current_distance
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dir_y, dir_x in directions:
                next_y = i + dir_y
                next_x = j + dir_x
                if 0 <= next_y < size and 0 <= next_x < size and mapping[next_y][next_x] != "#":
                    q.append((next_y, next_x))


        current_distance += 1
    
    if byte_number - 1 == number_bytes:
        answer_1 = distance[(size-1, size-1)]
    if distance[(size-1, size-1)] == sys.maxsize:
        answer_2 = f"{x},{y}"
        break

    


print(f"answer_1 = {answer_1}")
print(f"answer_2 = {answer_2}")

