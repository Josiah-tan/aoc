file_number = 2
part_1 = False
import re
from competitive import Point, sign, showMap

from itertools import product

# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n\n')
print(f"entries = {entries}")

mapping = entries[0]
if not part_1:
    mapping = re.sub("#", "##", mapping)
    mapping = re.sub("O", "[]", mapping)
    mapping = re.sub(r"\.", "..", mapping)
    mapping = re.sub("@", "@.", mapping)
mapping = [list(i) for i in mapping.split("\n")]
showMap(mapping)


directions = re.sub('\n', '', entries[1])

height = len(mapping)
width = len(mapping[0])


for i, j in product(range(height), range(width)):
    if mapping[i][j] == '@':
        pos = Point(i, j)


def quantify(direction):
    if direction == "^":
        return Point(-1, 0)
    if direction == ">":
        return Point(0, 1)
    if direction == "<":
        return Point(0, -1)
    if direction == "v":
        return Point(1, 0)


def moveIfCanMove(pos, direction):
    if (mapping[pos.y][pos.x] == "."):
        return True;
    if (mapping[pos.y][pos.x] == "#"):
        return False;
    if (mapping[pos.y][pos.x] == "O") and moveIfCanMove(pos + direction, direction):
        mapping[pos.y][pos.x], mapping[pos.y + direction.y][pos.x + direction.x] = mapping[pos.y + direction.y][pos.x + direction.x], mapping[pos.y][pos.x]
        return True;
    if (mapping[pos.y][pos.x] == "@") and moveIfCanMove(pos + direction, direction):
        mapping[pos.y][pos.x], mapping[pos.y + direction.y][pos.x + direction.x] = mapping[pos.y + direction.y][pos.x + direction.x], mapping[pos.y][pos.x]
        return True;

    if (mapping[pos.y][pos.x] == "]"):
        if direction.y == 0 and moveIfCanMove(pos + direction, direction):
            mapping[pos.y][pos.x], mapping[pos.y + direction.y][pos.x + direction.x] = mapping[pos.y + direction.y][pos.x + direction.x], mapping[pos.y][pos.x]
            return True;
        if direction.y != 0 and moveIfCanMove(pos + direction, direction) and moveIfCanMove(pos + direction + Point(0, -1), direction):
            mapping[pos.y][pos.x], mapping[pos.y + direction.y][pos.x + direction.x] = mapping[pos.y + direction.y][pos.x + direction.x], mapping[pos.y][pos.x]
            mapping[pos.y][pos.x - 1], mapping[pos.y + direction.y][pos.x + direction.x - 1] = mapping[pos.y + direction.y][pos.x + direction.x - 1], mapping[pos.y][pos.x - 1]
            return True;
        return False;
    if (mapping[pos.y][pos.x] == "["):
        if direction.y == 0 and moveIfCanMove(pos + direction, direction):
            mapping[pos.y][pos.x], mapping[pos.y + direction.y][pos.x + direction.x] = mapping[pos.y + direction.y][pos.x + direction.x], mapping[pos.y][pos.x]
            return True;
        if direction.y != 0 and moveIfCanMove(pos + direction, direction) and moveIfCanMove(pos + direction + Point(0, 1), direction):
            mapping[pos.y][pos.x], mapping[pos.y + direction.y][pos.x + direction.x] = mapping[pos.y + direction.y][pos.x + direction.x], mapping[pos.y][pos.x]
            mapping[pos.y][pos.x + 1], mapping[pos.y + direction.y][pos.x + direction.x + 1] = mapping[pos.y + direction.y][pos.x + direction.x + 1], mapping[pos.y][pos.x + 1]
            return True;
        return False;
    return False;

def showMap(mapping):
    print("\n".join(["".join(i) for i in mapping]))

showMap(mapping)
for direction in directions:
    if moveIfCanMove(pos, quantify(direction)):
        pos += quantify(direction)


showMap(mapping)

answer_1 = 0
for i, j in product(range(height), range(width)):
    if mapping[i][j] == "O":
        answer_1 += i * 100 + j

print(f"answer_1 = {answer_1}")

answer_2 = 0
for i, j in product(range(height), range(width)):
    if mapping[i][j] == "[":
        answer_2 += i * 100 + j
showMap(mapping)
print(f"answer_2 = {answer_2}")
1519991
