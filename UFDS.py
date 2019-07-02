# UFDS 
# Maneja 4 funciones:
# Inicializacion(initSet)
# quickFind(quickFindSet)
# Busqueda(findSet) Decir quien es su padre
# MismoSet(isSameSet)

# Inicializa un arreglo n
def initSet(n):
    return print([x for x in range(n)])


# Determina en que subconjunto se encuentra un elemento en particular.
def find(G, i):
    if G[i] == i:
        return i
    else:
        #G[i] = find(G,G[i])
        return find(G,G[i])

# Determina si los objetos a y b estan conectados
def isSame(G, a, b):
    fa = find(G,a)
    fb = find(G, b)
    if fa == fb:
        return True
    else:
        return False



# Complejidad: El algoritmo de Quick Find puede tomar MxN(tiempo de algoritmo) pasos para procesar M comandos de union sobre N objetos
def quickFind(G, a, b):
    fa = find(G, a)
    fb = find(G, b)
    if fa != fb: # / !isSame(a,b)
        G[fa] = fb
        n = len(G)
        for i in range(n):
            if G[i] == fa:
                G[i] = fb

# Complejidad La union puede ser muy costosa (N pasos). Los arboles pueden volverse muy altos. 
# Find puedes ser tambien muy costosa (N pasos). Necesario hacer Find para hacer Union.
def quickUnion(G, a, b):
    fa = find(G, a)
    fb = find(G, b)
    if fa != fb: # / !isSame(a,b)
        G[fa] = fb

# Mejoras:
# Mejora 1: Ponderacion
# Quick-Union ponderado: Modificar el algoritmo Quick-Union para evitar arboles altos. Mantener registro del tamaño de cada componente. Balancear conectando los arboles pequeños debajo del más grande.
def findPonderado(G, a):
    i = a
    while G[i] >= 0:
        i = G[i]
    return i


def quickUnionPonderado(G, a, b):
    fa = findPonderado(G, a)
    fb = findPonderado(G, b)
    if fa != fb:
        if G[fa] <= G[fb]:
            G[fa] += G[fb]
            G[fb] = fa
        elif G[fb] < G[fa]:
            G[fb] += G[fa]
            G[fa] = fb
    

import math 
INF = math.inf

def DefinirPuntoInicioYFin(G):
    n = len(G)
    maxi = -1
    pi = 0
    pf = 0
    for i in range(n):
        for v, w in G[i]:
            if w > maxi:
                maxi = w
                pi = i
                pf = v
    return pi, pf 

def Union(G, a, b):
    G[b] = a

def CheckHaveMin(G, s, path):
    mini = INF
    posFinal = -1
    for v, w in G[s]:
        if w < mini and (find(path, s) != find(path, v)):            
            mini = w
            posFinal = v
    if posFinal != -1:
        Union(path, s, posFinal)
    return posFinal
    

def UFDSModificado(G, s , e):
    n = len(G)
    path = [x for x in range(n)]
    order = []
    pos = s
    order.append(pos)
    for _ in range(n):
        pos = CheckHaveMin(G, pos, path)
        order.append(pos)
    if pos == e:
        return None
    else:
        order.append(s)
        return order 
    


        


