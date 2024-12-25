from itertools import product, combinations
file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n\n')


uniques = set()


answer_1 = 0
for entry in entries:
    mapping = entry.split("\n")
    height = len(mapping)
    width = len(mapping[0])

    unique = 0
    for i, j in product(range(height), range(width)):
        if mapping[i][j] == "#":
            unique |= 1 << (i * width + j)
    uniques.add(unique)


answer_1 = 0
for a, b in combinations(uniques, 2):
    answer_1 += a & b == 0
print(f"answer_1 = {answer_1}")
