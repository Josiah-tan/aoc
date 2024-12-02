file_number = 2

from competitive import sign
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

def isSafe(entry):
    signing = sign(entry[1] - entry[0])
    flag = 1
    for i in range(0, len(entry) - 1):
        diff = entry[i + 1] - entry[i]
        if signing != sign(diff):
            flag = 0
        elif abs(diff) < 1 or abs(diff) > 3:
            flag = 0
    return flag


summation = 0
for entry in entries:
    entry = list(map(int, entry.split(" ")))
    flag = isSafe(entry)
    summation += flag
print(f"summation = {summation}")


summation = 0
for entry in entries:
    entry = list(map(int, entry.split(" ")))
    flag = isSafe(entry)
    for i in range(len(entry)):
        flag |= isSafe(entry[:i] + entry[i+1:])
    summation += flag

print(f"summation = {summation}")
