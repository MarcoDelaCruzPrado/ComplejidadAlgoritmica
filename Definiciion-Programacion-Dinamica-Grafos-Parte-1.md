# Programacion Dinamicas en grafos parte 1.

>Objetivo:
Manejar y desarrollar los principios del paradigma de programacion deinamica para encontrar caminos minimos en grafos.

### Bellman Ford

* Algoritmo para grafos **ciclicos**
* Este algoritmo si funciona para **aristas negativas**
* Si el algoritmo encuentra que hay ciclos negativos alcanzables desde el origen, lanza una excepcion pues no posible hallar un SP para este caso.

>Codigo
```
def Bellman-Ford-Source(G, s):
    for i <- 1 to |V|- 1   // pasa |V| -| veces por los nodos
        foreach vertice(u, v) e E do:
            relax(u, v, W)
            foreach vertice(u, v) e E do:
                if d[v] > d[u] + w(u, v)
                    return false
            return true
```
### Floyd Warshall 

* Compara todos los posibles caminos a traves del grafo entre cada par de vertices.
* Ejecucion **O(n^3)**
* Programacion dinamica:
    * Grafo G con conjunto de vertices V (de 1 a N).
    * La matriz D[i, j]^(k): El camino minimo de i a j usando unicamente los vertices de 1 a k como puntos intermedios en el camino.
    * Ahora, dada esta funcion, nuestro objetivo es encontrar el camino minimo desde cada i a cada j usando unicamente los vertices de 1 hasta k + 1.

Dos posiblidades para el camino minimo:
* Utilizar unicamente los vertices (1....k) como puntos intermedios
* O, un camino que va desde i hasta k + 1, y de k + 1 hasta j. (el mas optimo claro).

```
                |   Wi,j                                           Si k = 0
  D [i,j]^(k)   |   
                |   min(D[i,j]^(k-1), D[i,k]^(k-1) + D[k,j]^(k-1))  Si k > 0
```

>Conclusion:

**Bellman Ford**
* Primero, el algoritmo calcula las distancias mas cortas que tiene a lo sumo 1 arista en el camino
* Luego, calcula las distancias mas cortas con que tienen a lo sumo 2 aristas en el camino y asi sucesivamente.
* Como maximo pueden haber |V| -1 aristas en un camino simple, ergo el algoritmo se ejecuta |V| -1 iteraciones

**Floyd-Warshall**
* Se inicializa la matriz solucion de igual manera que la matriz del grafo de entrada como primer paso.
* Luego, actualizamos la matriz solucion considerando cada vetice como un vertice intermedio.