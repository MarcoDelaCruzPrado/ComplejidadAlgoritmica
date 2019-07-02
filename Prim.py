import heapq as hq
import math
INF = math.inf

def prim(G):
    n = len(G)
    visited = [False]*n
    cost = [INF]*n
    path = [-1]*n
    order = []
    q = []
    a = 0
    hq.heappush(q, (0, a))
    order.append(a)
    cost[a] = 0
    while len(q) > 0:
        _, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for w, v in G[u]:
                if w < cost[v] and not visited[v]:
                    path[v] = u
                    cost[v] = w                   
                    order.append(v)
                    hq.heappush(q, (w, v))
    
    return order, path, cost

G = [ 
    [(5,1),(2,2),(6,4)] ,
    [(5,0),(4,2),(7,3),(9,5),(6,6)], 
    [(2,0),(4,1),(3,5),(6,6)],
    [(7,1),(8,7)],
    [(6,0),(9,6)],
    [(9,1),(3,2),(1,6)],
    [(6,1),(6,2),(9,4),(1,5)],
    [(8,3)]
]

o, p, c = prim(G)
print(o)
print("")
print(p)
print("")
print(c)