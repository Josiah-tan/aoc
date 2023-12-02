file_number = 1
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
print(f"entries = {entries}")

## part 1
max_colours = {"red": 12, "green": 13, "blue": 14}
game_number = 1
summation = 0
for game in entries:
    print(f"game {game_number}")
    add = 1;
    for draw in game.split(': ')[1].split('; '):
        # print(draw)
        colours = {};
        for pair in draw.split(', '):
            number, colour = pair.split(" ")
            colours[colour] = int(number);
            add = add and max_colours[colour] >= int(number)
    print(add * game_number)
    summation += add * game_number;
    game_number += 1;
print(summation)
    
## part 2
game_number = 1
summation = 0
for game in entries:
    print(f"game {game_number}")
    max_colours = {"red": 0, "green": 0, "blue": 0}
    for draw in game.split(': ')[1].split('; '):
        # print(draw)
        colours = {};
        for pair in draw.split(', '):
            number, colour = pair.split(" ")
            colours[colour] = int(number);
            max_colours[colour] = max(max_colours[colour], int(number));
    game_number += 1;
    print(max_colours["red"] * max_colours["green"] * max_colours["blue"])
    summation += max_colours["red"] * max_colours["green"] * max_colours["blue"]
print(summation)
