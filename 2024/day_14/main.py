import time
import re
from typing import DefaultDict
file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")
entries = [list(map(int, re.findall(r'[-\d]+', item))) for item in entries]


height = 103
width = 101

# height = 7
# width = 11


for seconds in range(7000, 8000):
    position_counter = DefaultDict(lambda: 0)
    
    for entry in entries:
        x, y, vx, vy = entry
        new_x = (x + (vx + width) * seconds) % width
        new_y = (y + (vy + height) * seconds) % height
        position_counter[(new_x, new_y)] += 1


    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0


    for (x, y), count in position_counter.items():
        # print(f"x = {x}")
        # print(f"y = {y}")
        # print(f"count = {count}")
        mid_height = height // 2
        mid_width = width // 2
        if x < mid_width:
            if y < mid_height:
                top_left += count
            elif y > mid_height:
                bottom_left += count
        elif x > mid_width:
            if y < mid_height:
                top_right += count
            elif y > mid_height:
                bottom_right += count





    safety_factor = top_left * top_right * bottom_left * bottom_right

    string = ""
    best = 0
    counter = 0
    for i in range(height):
        for j in range(width):
            if (j, i) in position_counter:
                string = string + "#"
                counter += 1
            else:
                string = string + "."
                best = max(counter, best)
                counter = 0
        string = string + "\n"
        counter = 0
    if best >= 10:
        print("\n" +string)
        print(seconds)
    if seconds % 1000 == 0:
        print(seconds)
    
