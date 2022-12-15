file_number = 2
part_2 = True
from personal import Point, sign
import numpy as np
with open(f'{file_number}.txt') as f:
    entries = [[list(map(int, i.split(","))) for i in a.split(" -> ")] for a in f.read().rstrip().split('\n')]
    max_y = max(max([point[1] for point in points]) for points in entries)
    max_x = max(max([point[0] for point in points]) for points in entries)
    entries = [[(Point(previous[0], previous[1]), Point(current[0], current[1])) for previous, current in zip(entry, entry[1:])] for entry in entries]
    matrix = np.array([['.' for _ in range(max_y + 1 + part_2)] for _ in range(max_x + max_x * part_2 + 1)])


for entry in entries:
    for current, previous in entry:
        direction = Point(sign(current.x - previous.x), sign(current.y - previous.y))
        matrix[previous.x][previous.y] = '#'
        for i in range(current.distanceManhattan(previous) + 1):
            new = direction * i + previous
            matrix[new.x][new.y] = '#'
            


counter = 0
finish = False
while True:
    point = Point(500, 0)
    if part_2 and matrix[point.x][point.y] == 'o':
        finish = True
        break;
    while True:
        if point.y == max_y + part_2:
            if part_2:
                matrix[point.x][point.y] = 'o'
                counter += 1
            else:
                finish = True
            break;
        elif matrix[point.x][point.y + 1] == '.':
            point += Point(0, 1)
        elif matrix[point.x - 1][point.y + 1] == '.':
            point += Point(-1, 1)
        elif matrix[point.x + 1][point.y + 1] == '.':
            point += Point(1, 1)
        else:
            matrix[point.x][point.y] = 'o'
            counter += 1
            break;
    
    if finish:
        break;

matrix[494:504,:10].transpose()
print(f"part {'2' if part_2 else '1'}: {counter}")

