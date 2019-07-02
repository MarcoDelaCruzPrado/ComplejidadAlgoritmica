import heapq as hq
import math
INF = math.inf

def find(G, a):
    if G[a] < 0:
        return a
    else:
        G[a] = find(G, G[a])
        return find(G, G[a])

def union(G, a, b):
    pa = find(G, a)
    pb = find(G, b)
    if pa != pb:
        if G[pa] <= G[pb]:
            G[pa] += G[pb]
            G[pb] = pa
        else:
            G[pb] += G[pa]
            G[pa] = pb

def MakeLi(G):
    li = []
    n = len(G)
    for u in range(n):
        for w, v in G[u]:
            li.append((w, u, v))
    return li

def kruskal(G):
    n = len(G)
    path = [-1]*n
    li = MakeLi(G)
    q = []
    T = []
    for edge in li:
        hq.heappush(q, edge)
    while len(q)>0:
        w, u, v = hq.heappop(q)
        if find(path, u) != find(path, v):
            union(path, u, v)
            T.append((w, v, u))
    return T

P = [ 
    [(5,1),(2,2),(6,4)] ,
    [(5,0),(4,2),(7,3),(9,5),(6,6)], 
    [(2,0),(4,1),(3,5),(6,6)],
    [(7,1),(8,7)],
    [(6,0),(9,6)],
    [(9,1),(3,2),(1,6)],
    [(6,1),(6,2),(9,4),(1,5)],
    [(8,3)]
]

T= kruskal(P)
print(T)
