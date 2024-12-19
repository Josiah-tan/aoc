file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n\n')

patterns = entries[0].split(", ")
print(f"patterns = {patterns}")
designs = entries[1].split("\n")
print(f"designs = {designs}")


##

answer_1 = 0
answer_2 = 0
for design in designs:
    dp = [0] * (len(design) + 1)

    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i - len(pattern) >= 0:
                if (design[i - len(pattern):i] == pattern):
                    dp[i] += dp[i - len(pattern)]

    answer_1 += dp[-1] > 0
    answer_2 += dp[-1]

print(f"answer_1 = {answer_1}")
print(f"answer_2 = {answer_2}")
