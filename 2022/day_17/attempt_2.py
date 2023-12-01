file_number = 2
part_1 = True
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    pattern = f.read().rstrip().split('\n')[0]
    # print(f"pattern = {pattern}")

def patternGenerator(pattern):
    while True:
        for character in pattern:
            yield character

placed = set(((x, 0) for x in range(7)))


top = 0

def getBlock(index, bottom):
    if index == 0:
        return set(((2, bottom), (3, bottom), (4, bottom), (5, bottom)))
    elif index == 1:
        return set(((3, bottom), (2, bottom + 1), (3, bottom + 1), (4, bottom + 1), (3, bottom + 2)))
    elif index == 2:
        return set(((4, bottom + 2), (4, bottom + 1), (2, bottom), (3, bottom), (4, bottom)))
    elif index == 3:
        return set(((2, bottom + 3), (2, bottom + 2), (2, bottom + 1), (2, bottom)))
    else:
        return set(((2, bottom + 1), (3, bottom + 1), (2, bottom), (3, bottom)))

pattern_generator = patternGenerator(pattern)

def move_left(block):
    if any(x == 0 for x, _ in block):
        return block
    else:
        return set((x - 1, y) for x, y in block)

def move_right(block):
    if any(x == 6 for x, _ in block):
        return block
    else:
        return set((x + 1, y) for x, y in block)

def move_up(block):
    return set((x, y + 1) for x, y in block)

def move_down(block):
    return set((x, y - 1) for x, y in block)

pattern_index = 0
seen = {}
t = 0
rocks = 1000000000000
answer_skipped = 0

while t < rocks:
    block = getBlock(t % 5, top + 4)
    while True:
        current_pattern = pattern[pattern_index]
        if current_pattern == "<":
            block = move_left(block)
            if block & placed:
                block = move_right(block)
        else:
            block = move_right(block)
            if block & placed:
                block = move_left(block)
        pattern_index = (pattern_index + 1) % len(pattern)
        block = move_down(block)
        if block & placed:
            block = move_up(block)
            placed |= block
            top = max(y for _, y in placed)

            placed_subset = (t % 5, pattern_index, frozenset((x, top - y) for (x, y) in placed if top - y <= 30))
            if placed_subset in seen and t >= 2022:
                top_old, t_old = seen[placed_subset]
                d_top = top - top_old  # height difference
                dt = t - t_old  # number of blocks
                print(f"rocks - t = {rocks - t}")
                answer_skipped += (rocks - t) // dt * d_top
                t += (rocks - t) // dt * dt
                print(f"t = {t}")
                assert t <= rocks
            seen[placed_subset] = (top, t)
            break;
    t += 1;
    if t == 2022:
        print(top)

print(top + answer_skipped)
