import re
from collections import defaultdict

rates  = {}
valves = {}

with open('1.txt') as f:
    for line in f:
        match = re.match(r'Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
        valve = match.group(1)
        rates[valve]  = int(match.group(2))
        valves[valve] = match.group(3).split(', ')

points = {('AA', (), 0)}

for _ in range(30):
    new_points = defaultdict(set)
    for valve, opened, pressure in points:
        pressure += sum(map(rates.get, opened))
        if valve not in opened and rates[valve]:
            new_points[(valve, tuple(sorted((*opened, valve))))].add(pressure)
        for dst in valves[valve]:
            new_points[(dst, opened)].add(pressure)
    points = {(valve, opened, max(pressures))
              for (valve, opened), pressures in new_points.items()}

print(max(pressure for *_, pressure in points))

