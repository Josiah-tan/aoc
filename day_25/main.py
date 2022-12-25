file_number = 2
part_1 = True
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
summation = 0
for entry in entries:
    length = len(entry)
    decimal = 0
    for i, char in enumerate(entry):
        value = 0
        if char.isdecimal():
            value = int(char) 
        elif char == "-":
            value = -1
        elif char == "=":
            value = -2
        decimal += value * 5 ** (length - 1 - i)
    summation += decimal

print(f"summation = {summation}")

result = ""

modulo = 1
while summation > 0:
    moduloed = summation % (5 * modulo)
    if moduloed > modulo * 2:
        moduloed -= modulo * 5
        summation -= moduloed
        if moduloed // modulo == -1:
            result = "-" + result
        elif moduloed // modulo == -2:
            result = "=" + result
    else:
        summation -= moduloed
        result = str(moduloed // modulo) + result
    modulo *= 5

    
    # result = str(summation % modulo) + result
    # summation -= summation % modulo
    # modulo *= 5

print(f"result = {result}")

