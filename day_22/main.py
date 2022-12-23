file_number = 2
part_1 = True
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
    board = entries[:-2]
    path = entries[-1]

def pathGenerator(path):
    string = ""
    for i in path:
        if i.isdecimal():
            string = string + i
        else:
            if len(string) != 0:
                yield int(string)
                string = ""
                yield i
    if len(string) != 0:
        yield int(string)


class Point:
    def __init__(self, y, x) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, obj):
        return Point(self.y + obj.y, self.x + obj.x)
    
    def __sub__(self, obj):
        return Point(self.y - obj.y, self.x - obj.x)
    
    def __repr__(self) -> str:
        return(f"P{self.y, self.x}")

direction_vector = {
        ">" : Point(0, 1),
        "v" : Point(1, 0),
        "<" : Point(0, -1),
        "^" : Point(-1, 0),
        }

direction_value = {
        ">" : 0,
        "v" : 1,
        "<" : 2,
        "^" : 3,
        }


next_direction = (">", "v", "<", "^")
direction = ">"
# y, x (zero indexed)

position = Point(0, board[0].find('.'))


for instruction in pathGenerator(path):
    if type(instruction) == int:
        for _ in range(int(instruction)):
            vector = direction_vector[direction]
            initial_position = position
            position += vector
            if direction == ">":
                if position.x == len(board[position.y]) or board[position.y][position.x] == " ":
                    # wrap around
                    for i in range(position.x):
                        if board[position.y][i] != " ":
                            position.x = i
                            break;
            elif direction == "v":
                if position.y == len(board) or position.x >= len(board[position.y]) or board[position.y][position.x] == " ":
                    for i in range(position.y):
                        if board[i][position.x] != " ":
                            position.y = i
                            break;
            elif direction == "<":
                if position.x == -1 or board[position.y][position.x] == " ":
                    for i in range(len(board[position.y]) - 1, position.x - 1, -1):
                        if board[position.y][i] != " ":
                            position.x = i
                            break;
            elif direction == "^":
                if position.y == -1 or position.x >= len(board[position.y]) or board[position.y][position.x] == " ":
                    for i in range(len(board) - 1, position.y - 1, -1):
                        if position.x < len(board[i]) and board[i][position.x] != " ":
                            position.y = i
                            break;
            
            if board[position.y][position.x] == "#":
                position = initial_position
    else:
        value = direction_value[direction]
        direction = next_direction[((1 if instruction == "R" else -1) + value) % len(next_direction)]


position += Point(1, 1)
answer = position.y * 1000 + position.x * 4 + direction_value[direction]
print(f"answer = {answer}")
