file_number = 1
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

entry = entries[0]
disk = [];
counter = 0
for i in range(len(entry)):
    if i & 1:
        disk += ['.'] * int(entry[i])
    else:
        disk += [str(counter)] * int(entry[i])
        counter += 1

i = 0;
j = len(disk)-1;

while (j > i):
    if disk[j] == '.':
        j -= 1
        continue;
    if disk[i] == '.':
        disk[i], disk[j] = disk[j], disk[i]
    i += 1


accumulator = 0
for i in range(len(disk)):
    if disk[i] == '.':
        break;
    accumulator += i * int(disk[i])

print(f"accumulator = {accumulator}")

## part 2
file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

entry = entries[0]
disk = [];
counter = 0
for i in range(len(entry)):
    if i & 1:
        disk += ['.'] * int(entry[i])
    else:
        disk += [str(counter)] * int(entry[i])
        counter += 1


right = len(disk) - 1
while right>=0:
    if disk[right] == '.':
        right-= 1;
    else:
        left = right;
        while left >= 0 and disk[left] == disk[right]:
            left -= 1
        
        
        i = 0;
        while i<len(disk):
            if disk[i] != '.':
                i += 1;
            else:

                if i > right:
                    break;
                
                j = i;
                while j < len(disk) and disk[j] == '.':
                    j += 1;

                
                if j - i >= right - left:
                    size = right - left
                    for k in range(size):
                        disk[right - k], disk[i + k] = disk[i + k], disk[right - k]
                    break;
                else:
                    i = j;

        right = left
        print(f"right = {right}")

accumulator = 0
for i in range(len(disk)):
    if disk[i] == '.':
        continue;
    accumulator += i * int(disk[i])

print(f"accumulator = {accumulator}")
