INF = 'inf'

def dfs(G, s, e):
    n = len(G)
    cam = []
    visited = [False]*n
    queued = [False]*n
    queued[s] = True
    q = [s]
    while len(q) > 0:
        u = q.pop()
        if not visited[u]:
            visited[u] = True
            cam.append(u)
            if u == e:
                break
            for v, w in reversed(G[u]):
                if not queued[v] and w > 0:
                    queued[v] = True
                    q.append(v)
    mini = INF
    nun = len(cam)
    for i in range(nun - 1):
        for v, w in G[cam[i]]:
            if v == cam[i+1] and w < mini:
                mini = w
    return cam, mini if visited[e] else None

def fordFulkerson(G, F):
    while True:
        c, mini = dfs(G, 0, 5) ## camino
        if mini == None: ## condicion de parada
            break
        nun = len(c)
        ## modifica el arrgelo flujo
        for i in range(nun-1):
            cont = -1
            for v, w in F[c[i]]:
                cont += 1
                if v == c[i+1]:
                    F[c[i]][cont] = (v, w + mini)
        ## modifica el arreglo original
        for i in range(nun-1):
            cont = -1
            for v, w in G[c[i]]:
                cont += 1
                if v == c[i+1]:
                    G[c[i]][cont] = (v, w - mini) ## resta la capacidad
                    cont = -1
                    ## crea los arcos opuestos
                    for u, w in G[v]:
                        cont += 1
                        if u == c[i]:
                            G[v][cont] = (c[i], mini + w) ## si ese arco ya existia aumenta la capacidad
                            cont = 10
                    if cont != 10:
                        G[v].append((c[i], mini)) ## si no existia lo crea
    return F

G = [[(1, 16), (3, 13)],
     [(2, 12), (3, 10)],
     [(3, 9), (5, 20)],
     [(1, 4), (4, 14)],
     [(2, 7), (5, 4)],
     []]

n = len(G)
F = [[] for _ in range(n)] ##grafo flujo
for u in range(n):
    for v, _ in G[u]:
        F[u].append((v, 0))

print(fordFulkerson(G, F))