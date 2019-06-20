import heapq as hq
import math
INF = math.inf

def dijstrak(G, a):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [INF]*n
    q = []
    cost[a] = 0
    hq.heappush(q, (0,a))
    while len(q) > 0:
        g, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v, w in G[u]:
                if not visited[v]:
                    f = w + g
                    if f < cost[v]:
                        path[v] = u
                        cost[v] = f
                        hq.heappush(q, (f,v))
    
    return path, cost





G = []
with open('grafito-prim.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums)//2):
            G[u].append((nums[i*2], nums[i*2+1]))
print(dijstrak(G,0))