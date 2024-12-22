from typing import DefaultDict


file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = list(map(int, f.read().rstrip().split('\n')))
print(f"entries = {entries}")

def mix(result, secret):
    return result ^ secret

def prune(secret):
    return secret % 16777216

def evolve(secret):
    result = secret * 64
    secret = mix(result, secret)
    secret = prune(secret)
    
    result = secret // 32
    secret = mix(result, secret)
    secret = prune(secret)

    result = secret * 2048
    secret = mix(result, secret)
    secret = prune(secret)
    return secret
    
answer_1 = 0

Q = DefaultDict(lambda: 0)

for entry in entries:
    prices = [entry % 10]
    changes = []
    score = {}
    for i in range(2000):
        entry = evolve(entry)
        prices.append(entry % 10)
        changes.append(prices[-1] - prices[-2])
        if i >= 3:
            pattern = (changes[i - 3], changes[i - 2], changes[i - 1], changes[i])
            if pattern in score:
                continue
            score[pattern] = prices[i + 1]
    answer_1 += entry
    for k, v in score.items():
        Q[k] += v

print(f"Q = {Q}")
answer_2 = max(Q.values())
