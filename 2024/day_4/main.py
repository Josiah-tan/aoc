file_number = 1
part_1 = True
from competitive import Point
from typing import List
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')

height = len(entries)
width = len(entries[0])
print(f"height = {height}")
print(f"width = {width}")

word = "XMAS"

directions:List[Point] = [
        Point(0, 1),
        Point(1, 1),
        Point(1, 0),
        Point(0, -1),
        Point(-1, -1),
        Point(-1, 0),
        Point(1, -1),
        Point(-1, 1),
              ]

summation = 0
for i in range(height):
    for j in range(width):
        for direction in directions:
            flag = True
            for k in range(len(word)):
                letter = word[k]
                offset:Point = direction * k
                offset_y = offset.y + i
                offset_x = offset.x + j
                if offset_y < 0 or offset_y >= height or offset_x < 0 or offset_x >= width:
                    flag = False
                    break
                if entries[offset_y][offset_x] != letter:
                    flag = False
                    break
            summation += flag

print(f"summation = {summation}")


## part 2


query_1 = ["M.S",".A.","M.S"]
query_2 = ["S.M",".A.","S.M"]
query_3 = ["M.M",".A.","S.S"]
query_4 = ["S.S",".A.","M.M"]

queries = [query_1, query_2, query_3, query_4]


summation = 0
for i in range(height):
    for j in range(width):
        for query in queries:
            matching = True
            for y in range(3):
                for x in range(3):
                    query_letter = query[y][x]
                    if query_letter == ".":
                        continue
                    if i + y < 0 or i + y >= height or j + x < 0 or j + x >= width:
                        matching = False
                    elif query_letter != entries[i + y][j + x]:
                        matching = False
            summation += matching
print(f"summation = {summation}")
