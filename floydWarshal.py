import math 
INF = math.inf

def floydWarshal(G):
    n = len(G)
    cost = [[INF for _ in range(n)] for _ in range(n)]
    path = [[-1 for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for w, v in G[u]:
            path[u][v] = u
            cost[u][v] = w

    for i in range(n):
        for u in range(n):
            for v in range(n):
                if i == u or u == v or i == v:
                    continue
                f = cost[u][i] + cost[i][v]
                if f < cost[u][v]:
                    cost[u][v] = f
                    cost[u][v] = i
    
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
