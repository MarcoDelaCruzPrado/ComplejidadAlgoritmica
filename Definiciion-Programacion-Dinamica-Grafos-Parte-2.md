# Programacion dinamica en grafos parte 2

>Objetivo:
Comprender los conceptos del Flujo Maximo y algoritmos de obtencio del mismo.

### **Camino minimo - Jhonson**

Se reduce a:
* 1 invocacion de iteracion de Bellman-Ford
* N invocaciones de Dijkstra

Dado un grafo Dirigido G(V, E), Obtenga G' de G añadiendo una constancia M a cada peso de arista. Cuando la longitud del camino entre un origen s y un destino t están garantizadas a ser las mismas en G' y en G?
* Cuando G no tiene ciclos negativos
* Cuando todas las aristas de G son no-negativas
* Cuando todos los caminos s-t en G tienen la misma cantidad de aristas
* Siempre camino minimo

Si a todas las aristas de un grafo, les sumo
```
C'e = Ce + Pu - Pv
```
Y habia antes un camino de s-t de longitud L, cual es la longitud del camino con las aristas modificadas?

**Pasos**
1. Primero, un Bellman-Ford desde un nodo inicial
2. Luego, cambiar todos los pesos de las aristas por los nuevos valores Pu y Pv
3. Ejecutar Dijkstra sobre todas las aristas restantes

### **Flujo de Redes**

Podemos representar problemas de flujo con grafos.
* Tuberias que son aristas que enlazan una serie de nodos. Cada tuberia tienen una capacidad especifica.
* Interconexiones de Redes. Cada enlace tiene una cierta capacidad de transmisión (Mbps).
* Otros problemas de asignación y distribución de horarios y/o actividades pueden ser resueltos con un Flujos.
* Cada arista tiene una Capacidad no negativa: C(u, v)
* Hay un nodo de Origen/Fuente (s) y uno de Destino/Sumidero (d)
* Los otros vertices solo son uniones
* El problema consiste en encontrar la maxima cantidad de flujo que puede ser llevado desde el nodo s al nodo d.
* EL flujo se preserva en todo momento "Todo flujo que entra debe salir"
* Existe una funcion F de flujo la cual indica la cantidad de flujo que transcurre por dicha arista.
```
f(u, v) <= c(u, v)
```
* El nodo de origen es el unico que produce flujo. Por lo tanto el flujo total de salida es:
```
|f| = Sumaf(s, v)
```

**Metodo de Ford-Fulkerson**
* Metodo para encontrar el Maximo Flujo
* Busca si hay un camino (Camino de aumento) del origen al detino llevando algo de flujo
* La cantidad de flujo esta determinada por la minima capacidad en una de las aristas del camino.
* Se usa un grafo de flujo Gf
* Se usa un grafo residual Gr.
* El grafo residual de un flujo tiene el mismo numero de vertices y puede tener uno o dos aristas por cada arista (u, v) original:
    * Arista con capacidad restante en la arista despues de llevar el flujo.
    * Arista contraria (v, u) con la cantidad de flujo.
* Merodo iterativo
* Se comienza con f(u, v) = 0 para cada par de nodos.
* En cada iteracion se incrementa el valor del flujo buscando un camino de aumento
* Un camino desde la fuente al sumidero que puede conducir mas flujo.
* En un camino simple de s a t en el grafo residual Gf.
* Cada arco (u, v) del camino aumentado admite algun flujo neto positivo.
* El flujo adicional maximo esta dado por:
```
Cf(p) = minCf(u, v) : (u, v) esta sobre p
```
* Se repite el proceso previo hasta no encontrar un camino de aumento.
* Capacidad residual: es la capacidad adicional del flujo que un arco puede llevar:
```
Cf(u, v) = c(u, v) - f(u, v)
```
* Dado una red de flujo G = (V, E) y un flujo f, la red residual incluida por f es Gf = (V, Ef), con
```
Ef = {(u, v) e V x V : cf(u, v) > 0}
```

**Algoritmo Ford Fulkerson**
```
inicializar flujo f a 0;
while exista un camino de aumneto p do:
    aumentar el flujo f a lo largo de p;
end
return f
```

>Conclusion

**Jhonson**
* Utiliza tanto Dijkstra como BellmanFord como subrutinas.
* La idea del algoritmo de Jhonson es volver a ponderar todos las aristas para resolverlas positivas, luego aplicar el algoritmo de Dijkstra para cada vertice.

**Flujos**
* ¿Que es un flujo en un grafo?
* ¿Cuales son las caracteristicas del Algoritmo de Ford-Fulkerson? Grafo residual. Camino de aumennto.
* Procedimiento del Ford-Fulkerson 
