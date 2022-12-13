from functools import cmp_to_key
from in2 import inputs
from in1 import inputs

class Pair:
    good = -1
    check = 0
    bad = 1


def goodPair(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return Pair.good
        elif left > right:
            return Pair.bad
        else:
            return Pair.check
    elif type(left) == list and type(right) == list:
        for (l, r) in zip(left, right):
            result = goodPair(l, r)
            if result == Pair.good:
                return Pair.good
            elif result == Pair.bad:
                return Pair.bad
        if len(left) < len(right):
            return Pair.good
        elif len(left) > len(right):
            return Pair.bad
        elif len(left) == len(right):
            return Pair.check
    elif type(left) == list and type(right) == int:
        return goodPair(left, [right])
    elif type(left) == int and type(right) == list:
        return goodPair([left], right)
    raise NotImplementedError


summation = 0
lefts = []
rights = []
for i in range(0, len(inputs) - 1, 2):
    left = inputs[i]
    right = inputs[i+1]
    lefts.append(left)
    rights.append(right)

for i in range(len(rights)):
    right = rights[i]
    left = lefts[i]
    if goodPair(left, right) == Pair.good:
        answer = i + 1
        summation += answer

print(f"summation = {summation}")


new = inputs + [[[2]], [[6]]]
sorted_list = sorted(new, key=cmp_to_key(goodPair))


multiply = 1
for i, value in enumerate(sorted_list):
    if value == [[2]] or value == [[6]]:
        multiply *= i + 1

print(f"multiply = {multiply}")

