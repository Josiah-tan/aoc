# thank you to smrq for this idea
# the original source code
# https://github.com/smrq/advent-of-code/blob/master/2022/22b.mjs
# the explanation
# https://www.reddit.com/r/adventofcode/comments/zsct8w/comment/j184mn7/?utm_source=share&utm_medium=web2x&context=3
# note for this one the naming is as follows:
# up → top face, down → bottom face

import re
from math import sqrt

directionsClockwise = ["east", "south", "west", "north"]
facesClockwise = {
        "u": ["r", "f", "l", "b"],
        "r": ["b", "d", "f", "u"],
        "f": ["r", "d", "l", "u"]
        }

direction2vector = {
        "south": (1, 0),
        "north": (-1, 0),
        "east": (0, 1),
        "west": (0, -1)
        }

facesClockwise["d"] = list(reversed(facesClockwise["u"]))
facesClockwise["l"] = list(reversed(facesClockwise["r"]))
facesClockwise["b"] = list(reversed(facesClockwise["f"]))

file_number = 2
part_1 = False
with open(f'{file_number}.txt') as f:
    full_map, instructions = f.read().rstrip().split('\n\n')
    instructions = re.findall(r"(\d+|\w)", instructions)
    instructions = list(map(lambda x: int(x) if x.isdecimal() else x, instructions))
    full_map = full_map.split("\n")
    number_faces = 6
    # literally just count number of "#" and "."
    size = int(sqrt(len(list(filter(lambda x: x != " ", "".join(full_map)))) / number_faces))
    
    total_width = max(len(line) for line in full_map) 
    total_height = len(full_map) 
    faces = []
    coordinate2face = []

    id = 0
    for i in range(total_height // size):
        coordinate2face.append([])
        for j in range(total_width // size):
            if len(full_map[i * size]) <= j * size or full_map[i * size][j * size] == " ":
                coordinate2face[i].append(None)
            else:
                coordinate2face[i].append(id)
                faces.append({
                    "i": i,
                    "j": j,
                    "map": [line[j * size : (j + 1) * size] for line in full_map[i * size : (i + 1) * size]],
                    "south": None,
                    "north": None,
                    "west": None,
                    "east": None,
                    "face": None,
                    })
                id += 1

# calculating the connections between the faces
def populateNeighbours(face, direction, neighbour):
    direction_index = directionsClockwise.index(direction)
    face_index = facesClockwise[face["face"]].index(neighbour)

    number_states = len(directionsClockwise)
    for i in range(number_states):
        face[directionsClockwise[(direction_index + i) % number_states]] = facesClockwise[face["face"]][(face_index + i) % number_states]

# hardcoding
faces[0]["face"] = "u"
populateNeighbours(faces[0], "east", "r")

visited = set()

# quick dfs to create connections
def walk(id):
    visited.add(id)

    i = faces[id]["i"]
    j = faces[id]["j"]


    for direction, vector in direction2vector.items():
        y = vector[0] + i
        x = vector[1] + j
        # if valid
        if y < total_height // size and x < total_width // size and y >= 0 and x >= 0:
            neighbour = coordinate2face[y][x]
            if neighbour and neighbour not in visited:
                faces[neighbour]["face"] = faces[id][direction]
                # populate the neighbour keeping in mind that in the opposite direction is the original face
                populateNeighbours(faces[neighbour], directionsClockwise[(directionsClockwise.index(direction) + 2) % len(directionsClockwise)], faces[id]["face"])
                walk(neighbour)
walk(0)

# print(faces)  # nice debugging

## initial position
id = 0
x = 0
y = 0
direction = "east"

for instruction in instructions:
    if instruction == "L":
        direction = directionsClockwise[(directionsClockwise.index(direction) + 3) % len(directionsClockwise)]
    elif instruction == "R":
        direction = directionsClockwise[(directionsClockwise.index(direction) + 1) % len(directionsClockwise)]
    else:
        for _ in range(instruction):
            vector = direction2vector[direction]
            
            new_y = y + vector[0]
            new_x = x + vector[1]
            new_id = id
            new_direction = direction
            
            if (new_y < 0 or new_x < 0 or new_y >= size or new_x >= size):
                new_x %= size
                new_y %= size
                new_face = faces[id][direction]
                for current_id in range(len(faces)):
                    if faces[current_id]["face"] == new_face:
                        new_id = current_id
                direction_index = directionsClockwise.index(direction)
                # while the direction is not facing opposite to the previous face
                while faces[new_id][directionsClockwise[(direction_index + 2) % 4]] != faces[id]["face"]:
                    # coordinate transformation: think about if you are walking East off the map, and end up South → [x, y] = [size - 1 - y, x]
                    [new_x, new_y] = [size - 1 - new_y, new_x]
                    direction_index = (direction_index + 1) % len(directionsClockwise)
                new_direction = directionsClockwise[direction_index]
            if faces[new_id]["map"][new_y][new_x] == "#":
                break;
            x = new_x;
            y = new_y
            id = new_id
            direction = new_direction

i = faces[id]["i"] * size + y + 1  # (+ 1 because zero indexed)
j = faces[id]["j"] * size + x + 1  # (+ 1 because zero indexed)
answer = 1000 * i + 4 * j + directionsClockwise.index(direction)
print(f"answer = {answer}")
