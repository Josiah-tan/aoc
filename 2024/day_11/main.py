from collections import defaultdict


file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip()
print(f"entries = {entries}")


def answer(blinks):
    stones = {i: 1 for i in entries.split(" ")}
    for _ in range(blinks):
        new_entries = defaultdict(lambda:0);
        for i in stones.keys():
            if i == '0':
                new_entries['1'] += stones[i]
            elif len(i) & 1 == 0:
                half = len(i)//2
                left = str(int(i[:half]))
                right = str(int(i[half:]))
                new_entries[left] += stones[i]
                new_entries[right] += stones[i]
            else:
                new_entries[str(int(i) * 2024)] += stones[i]
        stones = new_entries

    return sum(stones.values())

answer_1 = answer(25)
print(f"answer_1 = {answer_1}")

answer_2 = answer(75)
print(f"answer_2 = {answer_2}")
