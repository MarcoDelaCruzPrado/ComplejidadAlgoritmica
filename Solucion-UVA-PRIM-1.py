# link file:///D:/DATA%20DOWNLOAD/p10807.pdf
import math
import heapq as hq
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
    if  pa != pb:
        if G[pa] <= G[pb]:
            G[pa] += G[pb]
            G[pb] = pa
        else:
            G[pb] += G[pa]
            G[pa] = pb

def makeLi(G):
    n = len(G)
    li = []
    for u in range(n):
        for v, w  in G[u]:
            li.append((w, u, v))
    return li

def krukal(G):
    n = len(G)
    sumaA = 0
    sumaB = 0
    path = [-1]*n
    li = makeLi(G)
    q = []
    Ta = []
    Tb = []
    for edge in li:
        hq.heappush(q, edge)
    countA = 0
    while len(q) > 0:
        w, u, v = hq.heappop(q)
        if find(path, u) != find(path, v):
            union(path, u, v)
            Ta.append((w, u, v))
            sumaA += w
            countA += 1

    li = makeLi(G)
    q = []
    path = [-1]*n
    for edge in li:
        if edge not in Ta:
            hq.heappush(q, edge)
    countB = 0
    while len(q) > 0:
        w, u, v = hq.heappop(q)
        if find(path, u) != find(path, v):
            union(path, u, v)
            Tb.append((w, u, v))
            sumaB += w
            countB += 1
    if countA != n-1 or countB != n-1:
        print("no way")
    else:
        print(str(sumaA + sumaB))


G = [[(1,10),(1,30)],
[(0,20)]]

krukal(G)
