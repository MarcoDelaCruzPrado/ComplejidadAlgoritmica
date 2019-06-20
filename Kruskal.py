import heapq as hq

def find(G, a):
    if G[a] < 0:
        return a
    else:
        granpa = find(G, G[a])
        G[a] = granpa
        return granpa

def union(G,a,b):
    pa = find(G,a)
    pb = find(G,b)
    if pa != pb:
        if G[pa] <= G[pb]:
            G[pa] += G[pb]
            G[pb] = pa
        elif G[pb] < G[pa]:
            G[pb] += G[pa]
            G[pa] = pb

def makeIl(G):
    il = []
    n = len(G)
    for u in range(n):
        for v, w in G[u]:
            il.append((w, u, v))
    return il

def kruskal(G):
    il = makeIl(G)
    q = []
    n = len(G)
    for edge in il:
        hq.heappush(q,edge)

    path = [-1]*n
    T = []
    while len(q) > 0:
        w, u, v = hq.heappop(q)
        if find(path, u) != find(path, v):
            union(path, u, v)
            T.append((u,v,w))
    return path, T

G = []
with open('grafito-prim.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums)//2):
            G[u].append((nums[i*2],nums[i*2+1]))

print(kruskal(G))