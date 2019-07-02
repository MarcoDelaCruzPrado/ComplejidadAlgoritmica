import math 
INF = math.inf

def BellmanFord(G, s):
    n = len(G)
    cost = [INF]*n
    path = [-1]*n
    cost[s] = 0
    for _ in range(n-1):
        for u in range(n):
            for w, v in G[u]:
                f = cost[u] + w
                if f < cost[v]:
                    cost[v] = f
                    path[v] = u
    
    for u in range(n):
        for w, v in G[u]:
            f = cost[u] + w
            if f < cost[v]:
                return False,None, None

    return True, path, cost


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

_, path, cost = BellmanFord(P, 1)
print(path)
print("")
print(cost)