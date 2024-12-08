from itertools import permutations
from typing import DefaultDict

file_number = 2
part_1 = True
from competitive import Point
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')

height = len(entries) 
width = len(entries[0]) 

antinodes = set()
location_dict = DefaultDict(list)

for i in range(height):
    for j in range(width):
        char = entries[i][j]
        if char == '.':
            continue;
        else:
            location_dict[char].append(Point(i, j))

for char, locations in location_dict.items():
    for (a, b) in list(permutations(locations, 2)):
        node = (2 * a) - b
        if 0 <= node.x < width and 0 <= node.y < height:
            antinodes.add(node);

answer_1 = len(antinodes)
print(f"answer_1 = {answer_1}")
##

antinodes = set()
location_dict = DefaultDict(list)

for i in range(height):
    for j in range(width):
        char = entries[i][j]
        if char == '.':
            continue;
        else:
            location_dict[char].append(Point(i, j))

for char, locations in location_dict.items():
    for (a, b) in list(permutations(locations, 2)):
        difference = a - b
        resonance = 0
        while True:
            node = a + difference * resonance
            resonance+=1
            if 0 <= node.x < width and 0 <= node.y < height:
                antinodes.add(node);
            else:
                break;



answer_2 = len(antinodes)
print(f"answer_2 = {answer_2}")


