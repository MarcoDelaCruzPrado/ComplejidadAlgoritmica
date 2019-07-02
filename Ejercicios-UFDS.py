# UFDS Ejercicios
# Ejercicio 1

def Find(G, a):    
    if G[a] == a:
        return a
    else:
        return Find(G, G[a])

def Union(G, L, la, lb):
    a = BuscarLetra(L, la)
    b = BuscarLetra(L, lb)
    if a == None or b == None:
        print("Datos mal ingresados")
        return
    pa = Find(G, a)
    pb = Find(G, b)
    if pa != pb:
        print(la + " Ahora es amigo de "+ lb)
        for i in range(len(G)):
            if G[i] == pa:
                G[i] = pb
    else:
        print(la + " ya era amigo de " + lb)

def BuscarLetra(G, letter):
    for i in range(len(G)):
        if G[i] == letter:
            return i
    return None

def PrintConjunto(G, L):
    getConjunto = [[] for _ in range(len(G)) ] 
    for i in range(len(G)):
        getConjunto[G[i]].append(L[i])
    
    count = 1
    for i in range(len(G)):
        if len(getConjunto[i]) != 0:
            print('conjunto ' + str(count) + ': ')
            print(getConjunto[i])
            count += 1

#region Inpout
# L = ['a','b','c','d','e','f','g','h','i','j']
# G = [0,1,2,3,4,5,6,7,8,9]
# Union(G, L, 'a', 'b')
# Union(G, L, 'b', 'd')
# Union(G, L, 'c', 'f')
# Union(G, L, 'c', 'i')
# Union(G, L, 'j', 'e')
# Union(G, L, 'g', 'j')
# PrintConjunto(G, L)
#endregion

#Ejercicio 2

def FindMD(G, a):
    if G[a] == a:
        return a
    else:
        return FindMD(G, G[a])

def BuscarLetraMD(L, letter):
    for i in range(len(L)):
        if L[i] == letter:
            return i
    return None

def UnionMD(G, R, L, la, lb):
    a = BuscarLetraMD(L, la)
    b = BuscarLetraMD(L, lb)
    if a == None or b == None:
        print("Datos mal ingresados")
        return 
    pa = FindMD(G, a)
    pb = FindMD(G, b)
    if pa == pb:
        print(la + ' ya era amigo de ' + lb)
        return

    if pa != pb:
        if R[pa] <= R[pb]:
            G[b] = pa
            R[a] += R[b]
        else:
            G[a] = pb
            R[b] += R[a]

def PrintConjuntoMD(G, L):
    getConjunto = [[] for _ in range(len(G))]

    for i in range(len(G)):
        father = FindMD(G, i)
        getConjunto[father].append(L[i])
    
    count = 1
    for i in range(len(G)):
        if len(getConjunto[i]) > 0:
            print('conjunto ' + str(count) + ': ')
            print(getConjunto[i])
            count += 1

L2 = ['a','b','c','d','e','f','g','h','i','j']
G2 = [0,1,2,3,4,5,6,7,8,9]
R = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
UnionMD(G2, R, L2, 'a', 'b')
UnionMD(G2, R, L2, 'b', 'd')
UnionMD(G2, R, L2, 'c', 'f')
UnionMD(G2, R, L2, 'c', 'i')
UnionMD(G2, R, L2, 'j', 'e')
UnionMD(G2, R, L2, 'g', 'j')
print(R)
PrintConjuntoMD(G2, L2)