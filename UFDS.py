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
    


# G = [-1 for x in range(10)]
# quickUnionPonderado(G,3,4)
# print(G)
# quickUnionPonderado(G,4,9)
# print(G)
# quickUnionPonderado(G,8,0)
# print(G)
# quickUnionPonderado(G,2,3)
# print(G)
# quickUnionPonderado(G,5,6)
# print(G)
# quickUnionPonderado(G,5,9)
# print(G)
# quickUnionPonderado(G,7,3)
# print(G)
# quickUnionPonderado(G,4,8)
# print(G)
# quickUnionPonderado(G,6,1)
# print(G)

G = ['a','b','c','d','e','f','g','h','i','j']
n = len(G)
P = [x for x in range(n)]

def findFather(G, letter, P):
    n = len(G)
    for x in range(n):
        if letter == G[x]:
            if P[x] == x:
                return x
            else:
                return findFather(G, G[P[x]], P)

def UnionLetter(G, a, b, P):
    n = len(G)
    pa = findFather(G, a, P)
    pb = findFather(G, b, P)
    if pa != pb:
        P[pa] = P[pb]


print(P)
UnionLetter(G, 'a', 'b', P)
print(P)
UnionLetter(G, 'b', 'd', P)
print(P)
UnionLetter(G, 'c', 'f', P)
print(P)
UnionLetter(G, 'c', 'i', P)
print(P)
UnionLetter(G, 'j', 'e', P)
print(P)
UnionLetter(G, 'g', 'j', P)
print(P)


        


