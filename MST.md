# Arbol de expansión Minima (MST)

>Objetivo:
Obtener el arbol de axpansion minima de los grafos

Un **arbol de expansion** de un grafo G=(V, A) no dirigido y conexo es un subgrafo G'(V, A') **conexo y sin ciclos**

Los arboles de expansion en profundidad y en anchura de un grafo conexo.

En grafos con pesos el coste del arbol de expansion es la suma de los costes de las aristas.

**No es un arbol cuando:**
1. La red no es conexa.
2. Es una red con ciclo

Por lo que un arbol de expansión tiene que tener n nodos y n-1 arcos.

>Arbol de expansion minima / Arbol de cubrimiento minumo / Arbol recubridor minimo

Datos un grafo G = (V,A)
* No dirigido
* Valorado, con pesos no negativos

El arbol de expansion minima:
* Es un subgrafor G'=(V, A') conexo y sin ciclos
* Tal que la suma de sus aristas sea minima

Problema:
* Dado un grafo ponderado no dirigido, encontrar el arbol de expansion de menor coste.

Propiedad:
* Sea G=(V, A) un grafo conectado con pesos.
* Sea U un subconjunto del conjunto de vertices V.
    * **Si** e = (u, v)  es la arista de menor costo considerado que u pertenece a U y v pertenece a V-U
    * **Entonces** hay un arbol de expansion minima que incluye (u, v) como arista. 

* Algoritmos para resolver el problema:
    * Prim
    * Kruskal

* Ambos algoritmos
    * Utilizan la propiedad anterior
    * Son de tipo voraz: se selecciona uno de los candidatos con el criterio que es mejor en cada momento (menor costo)

## Algoritmo PRIM

1. Empezar en un vertice cualquiera **v**. El arbol consta inicialmente solo del nodo **v**.
2. En el resto de vertices, buscar el que este mas proximo a **v** (es decir, con la arista (v, w) de coste minimo). Añadir **w** y la arista (**v**,**w**) al arbol
3. Buscar el vertice mas proximo a cualquiera de estos dos. Añadir ese vertice y la arista al arbol del expansion.
4. Repetir sucesivamente hasta añadir los **n** vertices.

* El arbol T aumenta un vertice cada vez.
* El array d[v] contiene el menor costo de la arista que conecta v con el arbol.
* **Tiene uan complejidad O(n^2).**
* La solucion  se construye poco a poco, empezando con una solucion vacia.
* Implicitamente el algoritmo maneja los **conjuntos**:
    * **V**: vertices del grafo
    * **U**: vertices añadidos a la solucion
    * **V-U**: vertices que quedan por añadir
* ¿ Como implementar eficientemente la busqueda: encontrar el vertice de **V-U** mas proximo a alguno de los **U**?

## Algoritmo Kruskal

* Sea el grafo G = (V, A)
* Empeazar con un grafo sin aristar: G'=(V, 0)
* Seleccionar la arista de menor coste de A:
    * Si la arista seleccionada forma un ciclo en G', eliminarla.
    * Si no añadirla a G'.
* Repetir los dos pasos anteriores hasta tener n-1 aristas
* ¿ Como saber si una arista (v, w) provocaria un ciclo en el grafo G'?
* Añade una arista cada vez por orden de peso
* Acepta una arista si no produce un ciclo
* Se implementa usando una cola de prioridad
* Tiene una complejidad **O(nlogn)**
* Sabemos que en el arbol de expansion minima deben aparecer todos los vertices de G
* Lo que no sabemos aun es que arcos escoger para unirlos
* Lo que a KRUSKAL le interesa elegir son los arcos, no los vertices, como en PRIM

**Implementacion del algoritmo**

* Necesitamos:
    * Ordenar las aristass de G, de menor a mayor: O(nlogn)
    * Saber si una arista dada (v, w) provocará un ciclo
* ¿ Como comparar rapidamente si (v, w) forman un ciclo?
    *Una arsta (v, w) forma un ciclo si v y w estan en el mismo componente conexo
* La relacion "estan en el mismo punto componenete conexo" es una relacion de equivalencia

>RESUMEN

**MST**:
* Subconjunto de aristas de un grao, tal que la suma de sus esta sea la menor posible
