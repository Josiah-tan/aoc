from queue import Queue
from collections import defaultdict
file_number = 1
part_1 = True
with open(f'in/{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')[1:]
    entries = [tuple(map(int, entry.split(" "))) for entry in entries]


seen = set()
edges = defaultdict(list)
for entry in entries:
    seen.add(entry)
    for direction in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        new_node = tuple(i + j for i, j in zip(entry, direction))
        if new_node in seen:
            edges[new_node].append(entry)
            edges[entry].append(new_node)


answer1 = len(seen) * 6 - sum(len(edge) for edge in edges.values()) 
print(f"answer1 = {answer1}")

##

max_x = max(x for x, _, _ in seen) + 1
max_y = max(y for _, y, _ in seen) + 1
max_z = max(z for _, _, z in seen) + 1
min_x = min(x for x, _, _ in seen) - 1
min_y = min(y for _, y, _ in seen) - 1
min_z = min(z for _, _, z in seen) - 1

air = set()
air.add((min_x, min_y, min_z))
visiting = Queue()
visiting.put((min_x, min_y, min_z))

answer2 = 0

while not visiting.empty():
    node = visiting.get()
    for direction in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        new_node = tuple(i + j for i, j in zip(node, direction))
        if all(i >= j for i, j in zip((max_x, max_y, max_z), new_node)) and  all(i <= j for i, j in zip((min_x, min_y, min_z), new_node)) and new_node not in air:
            if new_node in seen:
                answer2 += 1
            else:
                air.add(new_node)
                visiting.put(new_node)
print(f"answer2 = {answer2}")
