file_number = 2
part_1 = True
from typing import DefaultDict
from competitive import Point, sign
import sys
import heapq
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

height = len(entries)
width = len(entries[0])

start_pos:Point = Point(0, 0)
end_pos:Point = Point(0, 0)
start_direction = Point(0, 1)
for i in range(height):
    for j in range(width):
        if entries[i][j] == "S":
            start_pos = Point(i, j)
        elif entries[i][j] == "E":
            end_pos = Point(i, j)

distance = DefaultDict(lambda: sys.maxsize)
distance[(start_pos, start_direction)] = 0


heap = []
heapq.heappush(heap, (0, start_pos, start_direction))

directions = [Point(1, 0), Point(-1, 0), Point(0, 1), Point(0, -1)]

while heap:
    cost, pos, direction = heapq.heappop(heap)

    if cost > distance[(pos, direction)]:
        continue

    new_direction = direction.rotateAnticlockwise90()
    if cost + 1000 < distance[(pos, new_direction)]:
        distance[(pos, new_direction)] = cost + 1000
        heapq.heappush(heap, (cost + 1000, pos, new_direction))
    
    new_direction = direction.rotateClockwise90()
    if cost + 1000 < distance[(pos, new_direction)]:
        distance[(pos, new_direction)] = cost + 1000
        heapq.heappush(heap, (cost + 1000, pos, new_direction))

    new_pos = pos + direction
    if (
            0 <= new_pos.y < height and
            0 <= new_pos.x < width and
            entries[new_pos.y][new_pos.x] != '#' and
            cost + 1 < distance[(new_pos, direction)]
            ):
        distance[(new_pos, direction)] = cost + 1
        heapq.heappush(heap, (cost + 1, new_pos, direction))


answer_1 = sys.maxsize
best_directions = set()
for direction in directions:
    answer_1 = min(answer_1, distance[(end_pos, direction)])

for direction in directions:
    if answer_1 == distance[(end_pos, direction)]:
        best_directions.add(direction)

print(f"answer_1 = {answer_1}")


best = set()

from queue import Queue

q = Queue()

for direction in best_directions:
    q.put((end_pos, direction))

best

while not q.empty():
    pos, direction = q.get()
    if (pos, direction) in best:
        continue
    best.add((pos, direction))
    
    cost = distance[(pos, direction)]

    new_direction = direction.rotateAnticlockwise90()
    if cost - 1000 == distance[(pos, new_direction)]:
        q.put((pos, new_direction))

    new_direction = direction.rotateClockwise90()
    if cost - 1000 == distance[(pos, new_direction)]:
        q.put((pos, new_direction))

    new_pos = pos - direction
    if (
            0 <= new_pos.y < height and
            0 <= new_pos.x < width and
            entries[new_pos.y][new_pos.x] != '#' and
            cost - 1 == distance[(new_pos, direction)]
            ):
        q.put((new_pos, direction))
    


unique_positions = set()

for pos, direction in best:
    unique_positions.add(pos)

answer_2 = len(unique_positions)
print(f"answer_2 = {answer_2}")
