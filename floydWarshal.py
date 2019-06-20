import math
INF = math.inf

def floydWarshal(G):
    n = len(G)
    cost = [[INF for _ in range(n)] for _ in range(n)]
    path = [[-1 for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v, w in G[u]:
            cost[u][v] = w
            path[u][v] = u

    for i in range(n):
        for u in range(n):
            for v in range(n):
                if v == u or u == i or v == i: 
                    continue
                f = cost[u][i] + cost[i][v]
                if f < cost[u][v]:
                    path[u][v] = i
                    cost[u][v] = f
    return path, cost

G = []
with open('grafito-prim.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i*2], nums[i*2+1]))

# print(G)
print(floydWarshal(G))