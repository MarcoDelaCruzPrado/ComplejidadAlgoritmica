# UFDS Estructura de datos para conjuntos disjuntos

>Objetivo : *Manejar grupos eficientemente*

### Algoritmo Union-Find
Algoritmo que realiza operacion utiles en dicha estructura de datos.

**Find:** Detatermina en que subconjunto un elemento en particular. Esto se puede usar para determinar si dos elementos estan en un mismo subconjunto.

**Union:** Unir dos subconjuntos en un solo subconjunto.

Estas operaciones serviran oara la implementacion  del **ALGORITMO KRUSKAL** o problemas que involucren particionamiento como encontrar las componentes conexas en un grafo.

**Cualidades:**
1. Estructura de datos **(UNION)**
2. Permite identificar o rastrear elementos particionados en diferentes grupos o "sets" **(FIND)**
3. Util para detectar ciclos dentro de un grafo **(FIND)**
4. Internamento utiliza un arreglo de padres **(UNION y FIND)**
5. Maneja 4 funciones:
    1. Inicializacion (iniSet) -> Crear un arreglo de numero **n**
    2. Union (unionSet) -> Unir 2 subcnjunto en uno solo
    3. Busqueda (findSet) -> Decir quien es su padre
    4. MismoSet (isSameSet) -> compara con el findSet si ambos padres son lo mismo

>Objetivo : **Diseñar una estructura de datos eficiente para UNION-FIND**

**Complejidad**
1. Econtrar consultar Find y comandos Union puede estar entremezclado
2. El numero de operacion M puede ser enorme
3. El numero de objetos N puede ser enorme


**Implementacion de FIND por compresion de caminos**

```
def findMejorado(G, a):
    if G[a] == a:
        return a
    else: return G[a] = findMejordo(G, G[a])
```

### Algoritmo Quick-Find

```
def findSet(G, a):
    if G[a] == a:
        return a
    else:
        return findSet(G, G[a])

def UnionSet(G, a, b):
    pa = findSet(G, a)
    pb = findSet(G, b)
    if pa != pb:
        for i in range(len(G))
            if G[i] == pb
                G[i] = pa
```


>Complejidad: 
El algoritmo Quick-Find puede tomar MxN pasos para procesar M comandos de union sobre N objetos



### Algoritmo Quick-Union

>Codigo:

```
def iniSet(n):
    return [i for i in range(n)]

def findSet(G, a):
    if G[a] == a:
        return a
    else:
        return findSet(G, G[a])

def isSameSet(G, a, b):
    if findSet(G, a) == findSet(G, b):
        return True
    return False

def UnionSet(G, a, b):
    pa = findSet(G, a)
    pb = findSet(G, b)
    if pa != pb:
        G[pb] = pa
```


>Complejidad: 
1. La union puede ser muy constosa (N pasos).
2. Los arboles pueden volverse muy altos.
3. Find puede ser tambien muy costoso(N pasos).
4. Necesario hacer Find para hacer Union.


| algoritmo | Union | Find | 
| ----------- | ------| ----- | 
|  Quick Find      |   N  |    1  |
|  Quick Union      |  N*  |    N  |  
 