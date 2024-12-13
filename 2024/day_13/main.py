file_number = 2
part_1 = True
from sympy import symbols
import sympy
from solve import *
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = [i.split('\n') for i in f.read().rstrip().split('\n\n')]
print(f"entries = {entries}")

entries[0]

import re
answer_1 = 0
answer_2 = 0

for entry in entries:
    entry = [list(map(int, re.findall(r'\d+', item))) for item in entry]
    A_cost = 3
    B_cost = 1
    XA = entry[0][0]
    YA = entry[0][1]
    XB = entry[1][0]
    YB = entry[1][1]
    X = entry[2][0] + 10000000000000
    Y = entry[2][1] + 10000000000000
    i, j = symbols("i j")
    ans = solve([Eq(i * (XA) + j * (XB), X), Eq(i * (YA) + j * (YB), Y)])
    i, j = ans[i], ans[j]
    if type(i) == sympy.core.numbers.Rational or type(j) == sympy.core.numbers.Rational:
        continue;
    if not (i > 100 or j > 100):
        answer_1 += i * A_cost + j * B_cost
    answer_2 += i * A_cost + j * B_cost
answer_1
answer_2
