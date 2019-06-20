import heapq as hq
import math
INF = math.inf

def prim(G):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [INF]*n
    queue = []
    s = 0
    cost[s] = 0
    hq.heappush(queue,(0,s))
    while len(queue) > 0:
        _, u = hq.heappop(queue)
        if not visited[u]:
            visited[u] = True
            for v, w in G[u]:
                if not visited[v] and w < cost[v]:
                    path[v] = u
                    cost[v] = w
                    hq.heappush(queue, (w, v))

    return path, cost

G = []
with open('grafito-prim.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i * 2], nums[i * 2 + 1]))

print(G)