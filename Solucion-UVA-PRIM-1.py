# link file:///D:/DATA%20DOWNLOAD/p10807.pdf
import math
import heapq as hq
INF = math.inf

#region prim
# def prim(G):
#     n = len(G)
#     visited = [False]*n
#     path = [-1]*n
#     cost = [INF]*n
#     q = []
#     s = 0
#     cost[s] = 0
#     hq.heappush(q, (0,s))
#     while len(q) > 0:
#         _, u = hq.heappop(q)
#         if not visited[u]:
#             visited[u] = True
#             for v, w in G[u]:
#                 if not visited[v] and w > cost[v]:
#                     cost[v] = w
#                     path[v] = u
#                     hq.heappush(q, (w, v))  

#     suma = 0
#     for x in cost:
#         if x == INF:
#             print("¡De ninguna manera!")
#             return
#         else:
#             suma += x
#     print(str(suma))
#     return
#endregion

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