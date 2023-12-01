file_number = 2
part_1 = True
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
summation = 0
for entry in entries:
    length = len(entry)
    decimal = 0
    for i, char in enumerate(entry):
        decimal += {"-": -1, "=": -2, "0": 0, "1": 1, "2": 2}[char] * 5 ** (length - 1 - i)
    summation += decimal

print(f"summation = {summation}")

result = ""

while summation > 0:
    result = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}[(summation + 2) % 5 - 2] + result
    summation = round(summation / 5)
print(f"result = {result}")
    
