# INF = 'inf'

# def dfs(G, s, e):
#     n = len(G)
#     cam = []
#     visited = [False]*n
#     queued = [False]*n
#     queued[s] = True
#     q = [s]
#     while len(q) > 0:
#         u = q.pop()
#         if not visited[u]:
#             visited[u] = True
#             cam.append(u)
#             if u == e:
#                 break
#             for v, w in reversed(G[u]):
#                 if not queued[v] and w > 0:
#                     queued[v] = True
#                     q.append(v)
#     mini = INF
#     nun = len(cam)
#     for i in range(nun - 1):
#         for v, w in G[cam[i]]:
#             if v == cam[i+1] and w < mini:
#                 mini = w
#     return cam, mini if visited[e] else None

# def fordFulkerson(G, F):
#     while True:
#         c, mini = dfs(G, 0, 5) ## camino
#         if mini == None: ## condicion de parada
#             break
#         nun = len(c)
#         ## modifica el arrgelo flujo
#         for i in range(nun-1):
#             cont = -1
#             for v, w in F[c[i]]:
#                 cont += 1
#                 if v == c[i+1]:
#                     F[c[i]][cont] = (v, w + mini)
#         ## modifica el arreglo original
#         for i in range(nun-1):
#             cont = -1
#             for v, w in G[c[i]]:
#                 cont += 1
#                 if v == c[i+1]:
#                     G[c[i]][cont] = (v, w - mini) ## resta la capacidad
#                     cont = -1
#                     ## crea los arcos opuestos
#                     for u, w in G[v]:
#                         cont += 1
#                         if u == c[i]:
#                             G[v][cont] = (c[i], mini + w) ## si ese arco ya existia aumenta la capacidad
#                             cont = 10
#                     if cont != 10:
#                         G[v].append((c[i], mini)) ## si no existia lo crea
#     return F

# G = [[(1, 16), (3, 13)],
#      [(2, 12), (3, 10)],
#      [(3, 9), (5, 20)],
#      [(1, 4), (4, 14)],
#      [(2, 7), (5, 4)],
#      []]

# n = len(G)
# F = [[] for _ in range(n)] ##grafo flujo
# for u in range(n):
#     for v, _ in G[u]:
#         F[u].append((v, 0))

# print(fordFulkerson(G, F))

from math import inf

def ford(G, s, t):
  n = len(G)
  Gb = [[] for _ in range(n)]     # Grafo con aristas bidirigidas
  f = [[0]*n for _ in range(n)]   # Flujo actual
  c = [[0]*n for _ in range(n)]   # Capacidad
  fmax = 0                        # Flujo máximo
  for u in range(n):
    for v, fm in G[u]:
      Gb[u].append((v, True))
      Gb[v].append((u, False))
      c[u][v] = fm
  
  def rec(vis, u, t, edg, cf):
    if u == t:
      return edg, cf
    vis[u] = True
    for v,p in Gb[u]:
      if vis[v]:
        continue
      ca = c[u][v]-f[u][v]
      if not p:
        ca = f[v][u]
      if ca == 0:
        continue
      _edg, fm = rec(vis, v, t, edg + [(u,v,p)], min(cf, ca))
      if len(_edg) != 0:
        return _edg, fm
    return [], 0
  
  while 1:
    a, cf = rec([False]*n, s, t, [], inf)
    if len(a) == 0:
      break
    for u,v,p in a:
      if p:
        f[u][v] += cf
      else:
        f[v][u] -= cf
    fmax += cf
  return fmax

T = [
  [(2,5),(3,3)],
  [(4,4)],
  [(4,3),(1,3),(3,3)],
  [(1,5)],
  []
]

print(ford(T, 0, 4))
