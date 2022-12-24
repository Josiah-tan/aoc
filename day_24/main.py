from collections import defaultdict


file_number = 3
part_1 = True
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
    entries = [entry[1:-1] for entry in entries[1:-1]]


width = len(entries[0])
height = len(entries)

arrow_vector = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

initial_arrows = {}
for i in range(height):
    for j in range(width):
        if entries[i][j] == ".":
            continue
        initial_arrows[(i, j)] = [entries[i][j]]

def calculatePosition(initial_arrows, time):
    current_arrows = defaultdict(list)

    for (y, x), arrows in initial_arrows.items():
        for arrow in arrows:
            i, j = arrow_vector[arrow]
            current_arrows[((y + i * time) % height, (x + j * time) % width)].append(arrow)
    return current_arrows

def drawPosition(initial_arrows, time):
    current_arrows = calculatePosition(initial_arrows, time)
    result = []
    for i in range(height):
        string = ""
        for j in range(width):
            if (i, j) in current_arrows:
                if len(current_arrows[(i, j)]) == 1:
                    string += current_arrows[(i, j)][0]
                else:
                    string += str(len(current_arrows[(i, j)]))
            else:
                string += "."
        result.append(string)
    return result

# for i in range(6):
#     print("#" * 5)
#     print(f"iteration i = {i}")
#     string = drawPosition(initial_arrows, i);
#     print(f"string = \n{string}")


def solve(start, goal, minute):
    states = {(start)}
    while True:
        minute += 1
        new_states = set()
        print(minute, len(states), max(i for i, j in states), max(j for i, j in states))
        for y, x in states:
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                new_y = y + i
                new_x = x + j
                if (new_y, new_x) == goal:
                    return minute
                current_position = calculatePosition(initial_arrows, minute)
                if (new_y, new_x) == start or (new_y >= 0 and new_x >= 0 and new_y < height and new_x < width and (new_y, new_x) not in current_position):
                    new_states.add((new_y, new_x))
        # states = new_states
        states = set(sorted(new_states, key=lambda pos: abs(pos[0] - goal[0]) + abs(pos[1] - goal[1]))[:100])

initial_x = 0
initial_y = -1
minute = 0

start = (initial_x, initial_y)
goal = (height, width - 1)
first_time = solve(start, goal, 0)
print(f"first_time = {first_time}")
second_time = solve(goal, start, first_time)
print(f"second_time = {second_time}")
third_time = solve(start, goal, second_time)
print(f"third_time = {third_time}")
