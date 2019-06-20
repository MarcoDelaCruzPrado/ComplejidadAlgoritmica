import math
INF = math.inf

def bellmannford(G, a):
    n = len(G)
    cost = [INF]*n
    path = [-1]*n
    cost[a] = 0
    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                f = cost[u] + w
                if f < cost[v]:
                    cost[v] = f
                    path[v] = u

    for u in range(n):
        for v, w in G[u]:
            f = cost[u] + w
            if f < cost[v]:
                return False, None, None

    return True, path, cost





G = []
with open('grafito-prim.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i*2], nums[i*2+1]))

print(bellmannford(G,0))