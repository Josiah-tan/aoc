file_number = 2
part_1 = True

with open(f'{file_number}.txt') as f:
    entries = f.read()

import re

def part1(entries):
    answer = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", entries)
    return sum(map(lambda x: (int(x[0]) * int(x[1])), answer))


part_1_solution = part1(entries)
print(f"part_1_solution = {part_1_solution}")

##

listing = []
enabled = True
for i in range(len(entries)):
    if entries[i:].startswith('do()'):
        enabled = True
    if entries[i:].startswith("don't()"):
        enabled = False
    if enabled:
        listing.append(entries[i])


part_2_solution = part1("".join(listing))
print(f"part_2_solution = {part_2_solution}")

