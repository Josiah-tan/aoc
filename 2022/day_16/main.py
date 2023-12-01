import numpy as np
import json

from queue import Queue
import re
file_number = 2
part_1 = True
# from personal import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = f.read().rstrip().split('\n')
    

def generator(entries):
    for entry in entries:
        # print(f"entry = {entry}")
        name, flow, tunnels = re.match("Valve ([A-Z]*) has flow rate=(\\d*); tunnels? leads? to valves? (.*)", entry).groups()
        tunnels = tunnels.split(", ")
        yield name, int(flow), tunnels


locs = {}
paths = {}
for name, flow, tunnels in generator(entries):
    locs[name] = {"rate": flow, "tunnels": tunnels}



for name in locs.keys():
    q = Queue()
    q.put(name)
    seen = set()
    seen.add(name)
    dist = {name: 0}

    while not q.empty():
        n = q.get()
        d = dist[n]
        for tunnel in locs[n]["tunnels"]:
            if (tunnel not in seen):
                seen.add(tunnel)
                dist[tunnel] = d + 1
                q.put(tunnel)
    paths[name] = dist
# print(f"paths = {paths}")

nonzero = [k for k, v in locs.items() if v["rate"] > 0]
# print(f"nonzero = {nonzero}")

dp = np.zeros((31, len(nonzero), 1 << len(nonzero))) - 999999
prev = np.empty((31, len(nonzero), 1 << len(nonzero)), dtype=object)

for i in range(len(nonzero)):
    dist = paths[nonzero[i]]["AA"]
    dp[dist + 1][i][1 << i] = 0

def getFlow(mask):
    sum = 0
    for i in range(len(nonzero)):
        if (mask & (1 << i) != 0):
            sum += locs[nonzero[i]]["rate"]
    return sum

ans = 0

for i in range(1, 31):
    for j in range(1 << len(nonzero)):
        for k in range(len(nonzero)):
            flow = getFlow(j)
            
            hold = dp[i-1][k][j] + flow
            if hold > dp[i][k][j]:
                dp[i][k][j] = hold
                prev[i][k][j] = [i-1, k, j]

            ans = max(ans, dp[i][k][j])

            if ((1 << k) & j) == 0:  # if k is closed
                continue;

            for l in range(len(nonzero)):
                if ((1 << l) & j) != 0:  # if l is open, no point going there
                    continue
                
                dist = paths[nonzero[k]][nonzero[l]]

                if (i + dist + 1) > 30:
                    continue;

                value = dp[i][k][j] + flow * (dist + 1)
                if value > dp[i + dist + 1][l][(1 << l) | j]:
                    dp[i + dist + 1][l][(1 << l) | j] = value
                    prev[i + dist + 1][l][(1 << l) | j] = [i, k, j]

print(f"ans = {ans}")

##
ans2 = 0
for i in range(1 << len(nonzero)):
    for j in range(1 << len(nonzero)):
        # if ((i & j)) != j:  # hurts brain
        if ((i & j)) != 0: # makes sure sets are unique hence are disjoint sets
            continue
        a = -99999999
        b = -99999999
        for k in range(len(nonzero)):
            a = max(a, dp[26][k][j])
        for k in range(len(nonzero)):
            # b = max(b, dp[26][k][i & ~j])  # hurts brain
            b = max(b, dp[26][k][i])
        ans2 = max(ans2, a + b)

print(f"ans2 = {ans2}")
