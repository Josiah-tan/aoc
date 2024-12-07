file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')

summation = 0
for entry in entries:
    test, numbers = entry.split(": ")
    test = int(test)
    numbers = list(map(int, numbers.split(" ")))

    length = len(numbers)


    for i in range(1 << (length - 1)):
        result = numbers[0];
        for j in range(length - 1):
            if i & (1 << j):
                result += numbers[j + 1]
            else:
                result *= numbers[j + 1]
        
        if result == test:
            summation += result;
            break;

print(f"summation = {summation}")



## part 2

summation = 0
for entry in entries:
    test, numbers = entry.split(": ")
    test = int(test)
    numbers = list(map(int, numbers.split(" ")))
    length = len(numbers)

    for i in range(3 ** (length - 1)):
        result = numbers[0];
        for j in range(length - 1):
            remainder = i % 3
            if remainder == 0:
                result += numbers[j + 1]
            elif remainder == 1:
                result *= numbers[j + 1]
            else:
                result = int(str(result) + str(numbers[j + 1]))
            i //= 3
        if result == test:
            print(f"result = {result}")
            summation += result;
            break;

print(f"summation = {summation}")





