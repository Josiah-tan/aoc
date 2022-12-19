import re
file_number = 1
part_1 = True
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')

def generator(entries):
    for entry in entries:
        entry = list(map(int, re.match("Blueprint (\\d*): Each ore robot costs (\\d*) ore. Each clay robot costs (\\d*) ore. Each obsidian robot costs (\\d*) ore and (\\d*) clay. Each geode robot costs (\\d*) ore and (\\d*) obsidian.", entry).groups()))
        blueprint = entry[0]
        
        ore_robot = (entry[1], 0, 0)
        clay_robot = (entry[2], 0, 0)
        obsidian_robot = (entry[3], entry[4], 0)
        geode_robot = (entry[5], 0, entry[6])
        
        yield blueprint, (ore_robot, clay_robot, obsidian_robot, geode_robot)
##

def mineOre(robots):
    return (robots[0:3], robots[-1])

def spendCombinations(robots, commodities, specifications):
    yield ((0, 0, 0, 0), commodities)
    for robot_index, specification in enumerate(specifications):
        remaining_commodities = tuple(commodity - requirement for commodity, requirement in zip(commodities, specification))
        if all(value >= 0 for value in remaining_commodities):
            for new_robots, c in spendCombinations(robots, remaining_commodities, specifications):
                robots_final = list(new_robots)
                robots_final[robot_index] += 1
                yield tuple(robots_final), c

def prune(states, specifications):
    new_states = {}
    # for (robots, commodities), geode in states.items():
    #     max_specifications = (max(i, j, k, l) for i, j, k, l in zip(*specifications))
    #     if all(robot <= max_specification for robot, max_specification in zip(robots[0:3], max_specifications)):
    #         new_states[(robots, commodities)] = geode
    new_states = tuple((robots, commodities, geode) for (robots, commodities), geode in states.items())
    def compare(state):
        robot, commodities, geode = state
        return robot[0] + robot[1] * 2 + robot[2] * 3 + robot[3] * 10 + commodities[0] + commodities[1] * 2 + commodities[2] * 3 + geode * 10
    new_states = sorted(new_states)[:min(len(new_states), 1000)]
    return {(robots, commodities): geode for (robots, commodities, geode) in new_states}

answer = 0
result = 0
for blueprint, specifications in generator(entries):
    minutes = 24
    states = {}
    states[((1, 0, 0, 0), (0, 0, 0))] = 0
    for time in range(1, minutes + 1):
        print("---")
        print(time)
        new_states = {}
        for (robots, commodities), geodes in states.items():
            # print(f"robots, commodities, geodes = {robots, commodities, geodes}")
            new_commodities, new_geodes = mineOre(robots)
            # print(f"new_commodities, new_geodes = {new_commodities, new_geodes}")
            counter = 0
            for new_robots, remaining_commodities in spendCombinations(robots, commodities, specifications):
                counter += 1
                # print(f"new_robots, remaining_commodities = {new_robots, remaining_commodities}")
                total_commodities = tuple(i + j for i, j in zip(new_commodities, remaining_commodities))
                total_robots = tuple(i + j for i, j in zip(new_robots, robots))
                total_geodes = new_geodes + geodes
                if (total_robots, total_commodities) not in new_states or new_states[(total_robots, total_commodities)] < total_geodes:
                    new_states[(total_robots, total_commodities)] = total_geodes
            result = max(counter, result)
        states = new_states
        # states = prune(new_states, specifications)
        print(len(states))
    temporary_answer = max(geodes for geodes in states.values())
    print(f"temporary_answer = {temporary_answer}")
    answer += blueprint * temporary_answer 
    print(f"result = {result}")

print(f"answer = {answer}")


