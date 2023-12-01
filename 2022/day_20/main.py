from collections import deque
from copy import deepcopy
file_number = 2
part_1 = False
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')

decryption = 1 if part_1 else 811589153
X = [int(x) * decryption for x in entries]
X = deque(list(enumerate(X)))

for t in range(1 if part_1 else 10):
    for i in range(len(X)):
        while X[0][0] != i:
            X.append(X.popleft())
        value = X.popleft()
        for j in range(value[1] % len(X)):
            X.append(X.popleft())
        X.append(value)

for i in range(len(X)):
    if X[i][1] == 0:
        answer = X[(i + 1000) % len(X)][1] + X[(i + 2000) % len(X)][1] + X[(i + 3000) % len(X)][1]
        print(f"answer = {answer}")
        break;
