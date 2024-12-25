from collections import deque


file_number = 2 
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n\n')
print(f"entries = {entries}")

inputs = {}

for wire, state in (entry.split(": ") for entry in entries[0].split("\n")):
    inputs[wire] = int(state)

inputs


queue = deque()

for input_1, gate, input_2, _,  output in (entry.split(" ") for entry in entries[1].split("\n")):
    queue.append([input_1, gate, input_2, output])


answer_1 = 0
while queue:
    input_1, gate, input_2, output = queue.popleft()
    if input_1 in inputs and input_2 in inputs:
        if gate == "XOR":
            inputs[output] = inputs[input_1] ^ inputs[input_2]
        if gate == "OR":
            inputs[output] = inputs[input_1] | inputs[input_2]
        if gate == "AND":
            inputs[output] = inputs[input_1] & inputs[input_2]

        if output.startswith("z"):
            answer_1 |= (1 << int(output[1:])) * inputs[output]

    else:
        queue.append([input_1, gate, input_2, output])



print(f"answer_1 = {answer_1}")

[i for i in inputs.keys() if i.startswith("y") or i.startswith("x")]

