# Programacion Dinamica (DP)

>Objetivo:
Mantener y desarrollar los principios del paradigma de progrmaacion dinamica.

* Programacion dinamica como divide y venceras, combinna soluciones a sub-problemas para hallar una solucion.
* Divde y venceras
    * Divide un problema en **partes independientes**
    * Resuelve cada parte
    * Combina las soluciones para resolver el problema original

**Pasos al diseñar un probelmas de DP**
1. Describe la estructura de una solucion optima. (Recurrencia)
2. Halle el valor de una solucion optima de abajo-hacia-arriba (Tabular)
3. Construya la solucion optima (Traceback)

Ejemplos:
### Numero de Fibonacci
* Se define a los numeros de Fibonacci como:
    * F0 = 0
    * F1 = 1
    * Fi = F(i-1) + F(i-2) para i > 1

```
def Fibonacci(i):
    array = []
    array.append(0)
    array.append(1)
    if i > 1:
        for x in range(2,i+1):
            array.append(array[x-1] + array[x-2])
    print(array[i])
```

* DP es aplicable cuando los problemas son independientes.
    * Los problemas comparten subproblemas
* Numeros Fibonacci:
    * Recurrenncia: F(n) = F(n-1) + F(n-2)
    * Limites: F(0) = 0, F(1) = 1
* Una acercamiento D&C resolveria repetidamente los subproblemas comunes.
* DP resuelve cada problema 1 vez y lo guarda en una tabla

### Cambio de monedas

* Cambiar n centavos con el **menor numero** de monedas.
* Analicemos el caso de Peru que tiene las monedas de centimos: