import heapq as hq
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

def jhonson(G):
    n = len(G)
    G.append([(0,0)])
    ok,_,h = bellmannford(G, n)
    if not ok:
        return False, None, None
    del G[-1]
    for u in range(n):
        for i in range(len(G[u])):
            v, w = G[u][i]
            w += h[u] - h[v]
            G[u][i] = (v, w)
        print(G[u])

    p = [None]*n
    c = [None]*n
    for u in range(n):
        p[u], c[u] = dijstrak(G, u)
    return p, c

G = []
with open('grafito-prim.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums)//2):
            G[u].append((nums[i*2], nums[i*2+1]))

p , c = jhonson(G)


