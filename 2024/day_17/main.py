import re
file_number = 1

# Parse input
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n\n')

registers = entries[0].split("\n")
program = entries[1]

A = int(re.findall(r"[-\d]+", registers[0])[0])
B = int(re.findall(r"[-\d]+", registers[1])[0])
C = int(re.findall(r"[-\d]+", registers[2])[0])

instructions = list(map(int, re.findall(r"[-\d]+", program)))

# Search for the lowest positive A
for j in range(1, 10**6):  # Adjust range as needed
    A = 117440
    B, C = 0, 0  # Reset registers
    outputs = []
    i = 0
    valid = True

    while valid:
        if i >= len(instructions):
            break
        instruction, operand = instructions[i], instructions[i + 1]
        
        # Compute combo operand
        if operand == 4:
            combo_operand = A
        elif operand == 5:
            combo_operand = B
        elif operand == 6:
            combo_operand = C
        elif operand == 7:
            valid = False
            break
        else:
            combo_operand = operand

        # Execute instruction
        if instruction == 0:
            A = A // (2 ** combo_operand)
            i += 2
        elif instruction == 1:
            B ^= operand
            i += 2
        elif instruction == 2:
            B = combo_operand % 8
            i += 2
        elif instruction == 3:
            if A == 0:
                i += 2
            else:
                i = operand
        elif instruction == 4:
            B ^= C
            i += 2
        elif instruction == 5:
            outputs.append(combo_operand % 8)
            i += 2
        elif instruction == 6:
            B = A // (2 ** combo_operand)
            i += 2
        elif instruction == 7:
            C = A // (2 ** combo_operand)
            i += 2

    # Check if outputs match instructions
    if outputs == instructions:
        answer_2 = A
        print(f"answer_2 = {answer_2}")
        break
