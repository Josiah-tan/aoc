
with open('2.in') as f:
    lines = [a.split() for a in f.read().rstrip().split('\n')]


class Directory:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.kids = {}
        self.sum = 0


root = Directory(None, None)

current = Directory(None, None)

i = 0
while i < len(lines):
    if lines[i][0] == "$":
        if lines[i][1] == "cd":
            if lines[i][2] == "/":
                root = Directory(None, "/")
                current = root
            elif lines[i][2] == "..":
                current = current.parent
            else:
                if lines[i][2] not in current.kids:
                    current.kids[lines[i][2]] = Directory(current, lines[i][2])
                current = current.kids[lines[i][2]]
            i += 1;
        elif lines[i][1] == "ls":
            i += 1
            while (i < len(lines) and lines[i][0] != "$"):
                if (lines[i][0].isdecimal()):
                    current.sum += int(lines[i][0])
                elif (lines[i][0] == "dir"):
                    if lines[i][1] not in current.kids:
                        current.kids[lines[i][1]] = Directory(current, lines[i][1])
                i += 1;



answer_1 = 0

cache = {}

def getSize(directory):
    global answer_1, cache
    solution = directory.sum + sum(getSize(v) for v in directory.kids.values())
    cache[directory.name] = solution
    if solution <= 100000:
        answer_1 += solution
    return solution

root_size = getSize(root)
print(f"root_size = {root_size}")
print(f"answer_1 = {answer_1}")
disk_space = 70000000
unused_space = disk_space - root_size
print(f"unused_space = {unused_space}")

amount_required = 30000000

amount_delete = amount_required - unused_space
print(f"amount_delete = {amount_delete}")

answer_2 = root_size
for value in cache.values():
    if value >= amount_delete and value < answer_2:
        answer_2 = value;
print(f"answer_2 = {answer_2}")

