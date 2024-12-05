from collections import defaultdict


file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')


print(f"entries = {entries}")

edges = []
queries = []
use_first = True
for entry in entries:
    if entry == "":
        use_first = False
        continue
    if use_first:
        edges.append(entry)
    else:
        queries.append(entry)

print(f"first = {edges}")
print(f"second = {queries}")
##

forward = defaultdict(list)
backward = defaultdict(list)


for f in edges:
    a, b = f.split('|')
    forward[a].append(b)
    backward[b].append(a)

from queue import Queue

part_1 = 0
part_2 = 0
for query in queries:
    numbers = query.split(",")
    okay = True
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            okay &= not numbers[j] in backward[numbers[i]]
    if okay:
        part_1 += int(numbers[len(numbers) // 2])
    else:
        final = []
        queue = Queue()
        numBehind = {number : len(set(backward[number]) & set(numbers)) for number in numbers}
        for number in numbers:
            if numBehind[number] == 0:
                queue.put(number)
        while not queue.empty():
            number = queue.get()
            final.append(number)
            for next in forward[number]:
                if next in numBehind:
                    numBehind[next] -= 1
                    if numBehind[next] == 0:
                        queue.put(next)
        part_2 += int(final[len(final)//2])

print(f"part_1 = {part_1}")
print(f"part_2 = {part_2}")
        






