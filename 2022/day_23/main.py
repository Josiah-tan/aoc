from collections import Counter
file_number = 3
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
# print(f"entries = {entries}")

elves = set()

for i, row in enumerate(entries):
    for j, value in enumerate(row):
        if value == "#":
            elves.add((i, j))


def getMapLayout(elves):
    min_elves_y = min(i for i, _ in elves)
    max_elves_y = max(i for i, _ in elves)
    max_elves_x = max(j for _, j in elves)
    min_elves_x = min(j for _, j in elves)
    solution = []
    for i in range(min_elves_y, max_elves_y + 1):
        solution.append("")
        for j in range(min_elves_x, max_elves_x + 1):
            solution[i - min_elves_y] += "#" if (i, j) in elves else "."
    return "\n".join(solution)


round_number = 0
while True:
    round_number += 1
    proposals = {}
    for elf in elves:
        i, j = elf
        elves_around = False
        for y, x in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if (y + i, x + j) in elves:
                elves_around = True
        if elves_around == False:
            continue
        
        for m in range(4):
            n = (round_number + m - 1) % 4
            no_elf = True
            if n == 0:  # North
                for y, x in [(-1, 0), (-1, 1), (-1, -1)]:
                    if (y + i, x + j) in elves:
                        no_elf = False
                if no_elf:
                    proposals[elf] = (i - 1, j + 0)
                    break;
            elif n == 1:  # South
                for y, x in [(1, 0), (1, 1), (1, -1)]:
                    if (y + i, x + j) in elves:
                        no_elf = False
                if no_elf:
                    proposals[elf] = (i + 1, j)
                    break;
            elif n == 2: # west
                for y, x in [(0, -1), (-1, -1), (1, -1)]:
                    if (y + i, x + j) in elves:
                        no_elf = False
                if no_elf:
                    proposals[elf] = (i, j - 1)
                    break;
            elif n == 3:  # east
                for y, x in [(0, 1), (-1, 1), (1, 1)]:
                    if (y + i, x + j) in elves:
                        no_elf = False
                if no_elf:
                    proposals[elf] = (i, j + 1)
                    break;
    counters = Counter([i for i in proposals.values()])
    new_elves = set()
    for elf in elves:
        if elf in proposals and counters[proposals[elf]] == 1:
            new_elves.add(proposals[elf])
        else:
            new_elves.add(elf)
    if new_elves == elves:
        # print_elves(elves)
        print(f"solution_2 = {round_number}")
        break;
    elves = new_elves
    # print("#" * 10)
    # print(f"round_number = {round_number}")
    if round_number == 10:
        map_layout = getMapLayout(elves)
        solution_1 = map_layout.count(".")
        print(f"solution_1 = {solution_1}")


