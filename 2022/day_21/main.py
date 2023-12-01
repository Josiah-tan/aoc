from sympy import *
import sympy
file_number = 2
part_2 = False

with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')

tree = {}

for entry in entries:
    left, right = entry.split(": ")
    right = right.split(" ")
    if part_2 and left == "humn":
        tree[left] = Symbol("x")
    else:
        tree[left] = right

print(tree)

def calculate(node):
    expression = tree[node]
    if part_2 and node == "root":
        return solve([Eq(calculate(expression[0]), calculate(expression[2]))])
    if type(expression) == sympy.core.symbol.Symbol:
        return expression
    elif len(expression) == 1:
        return int(expression[0])
    else:
        operation = expression[1]
        if operation == "+":
            return calculate(expression[0]) + calculate(expression[2])
        elif operation == "-":
            return calculate(expression[0]) - calculate(expression[2])
        elif operation == "*":
            return calculate(expression[0]) * calculate(expression[2])
        elif operation == "/":
            return calculate(expression[0]) / calculate(expression[2])

answer = calculate("root")
print(f"answer = {answer}")
