import math
import heapq as hq
INF = math.inf

def Dijkstra(G, s):
    n = len(G)
    cost = [INF]*n
    path = [-1]*n
    visited = [False]*n
    cost[s] = 0
    q = []
    hq.heappush(q, (0, s))
    while len(q) > 0:
        _, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for w, v in G[u]:
                if not visited[v]:
                    f = cost[u] + w
                    if f < cost[v]:
                        cost[v] = f
                        path[v] = u
                        hq.heappush(q, (f, v))
    return path, cost

    
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

path, cost = Dijkstra(P, 1)
print(path)
print("")
print(cost)