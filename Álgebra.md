# Explicación sobre el Álgebra del programa

---

**Recomiendo abrir este documento con un editor de Markdown o un programa que pueda visualizar archivos Markdown.**

---

**Este documento explica el funcionamiento del programa desde la perspectiva algebraica. Para acceder a información general sobre el programa, ve al documento [README.md](README.md).**

---

## Índice

1. [Las matrices en este programa](#las-matrices-en-este-programa)
   1. [La tabla de operaciones](#la-tabla-de-operaciones)
1. [Los sistemas de ecuaciones lineales en este programa](#los-sistemas-de-ecuaciones-lineales-en-este-programa)
2. [Funcionamiento del modo matricial](#funcionamiento-del-modo-matricial)
3. [Funcionamiento del modo ecuacional](#funcionamiento-del-modo-ecuacional)
4. [Algoritmos](#algoritmos)
   1. [Algoritmo de la matriz escalonada](#algoritmo-de-la-matriz-escalonada)
   2. [Ordenamiento de filas](#ordenamiento-de-filas)
   3. [Cálculo del rango](#cálculo-del-rango)
   4. [Cálculo del determinante](#cálculo-del-determinante)
   5. [Transposición de matrices](#transposición-de-matrices)
   6. [Generar matrices identidad de orden n](#generar-matrices-identidad-de-orden-n)
   7. [Transformar la matriz escalonada en la matriz identidad](#transformar-la-matriz-escalonada-en-la-matriz-identidad)
   8. [Inversión de matrices (algoritmo de Gauss)](#inversión-de-matrices-algoritmo-de-gauss)
5. [Operaciones elementales de filas](#operaciones-elementales-de-filas)
  1. [Multiplicar y dividir fila por constante](#multiplicar-y-dividir-fila-por-constante)
  2. [Intercambiar filas](#intercambiar-filas)
  3. [Restar y sumar filas](#restar-y-sumar-filas)
6. [Propiedades de las matrices](#propiedades-de-las-matrices)
7. [Propiedades de los sistemas de ecuaciones](#propiedades-de-los-sistemas-de-ecuaciones)
## Las matrices en este programa

En este programa las matrices son representadas como arrays bidimensionales. Como en el caso de Python no existen los arrays bidimensionales propiamente dichos, se simulan creando listas de listas.

En estos arreglos la primera dimensión son las filas de las matrices mientras la segunda dimensión son los elementos de las filas, es decir, el elemento de la columna j que se encuentra en la columna i. Es por esto que en el programa se suele referir a las filas como row y a los elementos como rowe (rowe = Row Element = elemento de fila).

Por ejemplo, la matriz
$$
\begin {bmatrix}
1 & 2 & 3 & 4\\
5 & 6 & 7 & 8\\
9 & 10 & 11 & 12\\
13 & 14 & 15 & 16
\end {bmatrix}
$$

sería representada en el programa como
$$
\begin{array}{ll}
[[1 & 2 & 3 & 4] 
[5 & 6 & 7 & 8] 
[9 & 10 & 11 & 12]
[13 & 14 & 15 & 16]]
\end{array}
$$

o, como código de Python: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]].

### La tabla de operaciones

La tabla de operaciones es una matriz irregular especial que guarda [las operaciones elementales de filas](#operaciones-elementales-de-filas) que se van realizando en el proceso de [transformar la matriz a procesar en la matriz identidad]((#transformar-la-matriz-escalonada-en-la-matriz-identidad)).

Las operaciones que están guardadas en la lista de operaciones se leen luego por la función invertMatrix para aplicárselas a la matriz identidad con tal de invertir la matriz.

Es una matriz irregular ya que es un array bidimensional en el que cada fila de la matriz es una operación que se ha realizado codificada, pero no todas las filas tienen el mismo número de elementos. Esto es porque las operaciones de multiplicar filas por constantes e intercambiar filas solo tienen 3 argumentos mientras la operación de resta de filas tiene 4 argumentos.

Así se guarda cada operación en la tabla:

|                 Operación                | Argumento 1 |     Argumento 2     |     Argumento 3     | Argumento 4 |
|:----------------------------------------:|:-----------:|:-------------------:|:-------------------:|:-----------:|
| Multiplicar y dividir fila por constante |      0      |  Índice de la fila  |        Factor       |             |
|            Intercambiar filas            |      1      | Índice de la fila 1 | Índice de la fila 2 |             |
|           Restar y sumar filas           |      2      | Índice de la fila 1 | Índice de la fila 2 |    Factor   |

Por ejemplo, la tabla de operaciones de la matriz invertible del ejercicio 3 de la entrega 6
$$
\begin {bmatrix}
1 & 0 & 3 & 3 \\
0 & 1 & 0 & 0 \\
1 & 0 & 4 & 3 \\
1 & 0 & 3 & 4
\end {bmatrix}
$$

sería representada en forma de matriz tal que así:
$$
\begin {bmatrix}
1 & 1 & 0 \\
1 & 0 & 1 \\
2 & 2 & 0 & 1 \\
2 & 3 & 3 & 1 \\
2 & 0 & 3 & 3 \\
2 & 0 & 2 & 3
\end {bmatrix}
$$

La matriz inversa que queda tras leer la tabla y aplicar las operaciones en orden a la matriz identidad es
$$
\begin {bmatrix}
7 & 0 & -3 & -3 \\
0 & 1 & 0 & 0 \\
-1 & 0 & 1 & 0 \\
-1 & 0 & 0 & 1
\end {bmatrix}
$$

## Los sistemas de ecuaciones lineales en este programa

En este programa los sistemas de ecuaciones no dejan de ser una extensión de las matrices. Son matrices fila de dos columnas en las que la primera columna es la lista de incógnitas de ese sistema en concreto mientras la segunda columna equivale la matriz que representa el sistema lineal pero transpuesta. Así, todas las filas de la matriz transpuesta excepto la última (la fila de las constantes) comparten índice con la incógnita de la lista de incógnitas de la que son coeficiente sus elementos.

Por ejemplo, el sistema de ecuaciones lineales
$$
\begin{cases}
-4\alpha - 2\beta - 3\omega = -1 \\
-2\alpha - 7\beta - \omega = 2 \\
\alpha - 4\beta + 5\omega = -2 \\
\end{cases}
$$

sería representado en el programa como
$$
\begin{array}{ll}
[[\alpha & \beta & \omega] 
[[-4 & -2 & 1] 
[-2 & -7 & -4]
[-3 & -1 & 5] 
[-1 & 2 & -2]]
\end{array}
$$

o, como código de Python: [['α', 'β', 'ω'], [[-4, -2, 1], [-2, -7, -4], [-3, -1, 5], [-1, 2, -2]]].

## Funcionamiento del modo matricial

1. Se lee [el archivo de entrada](README.md#opción-path-supmsup) y cada línea de [las matrices](README.md#matrices), que corresponed a una fila, se procesa y se añade a su entrada en la lista de matrices, que es un array tridimensional que es comparable a una matriz fila de matrices.
2. Una vez procesadas las matrices, se añade un número igual de entradas vacías a la lista de listas de propiedades de las matrices.
3. Se analiza cada matriz de la lista de matrices y se rellena su tabla de propiedades con las siguientes entradas:
   1. Se procesan todos los elementos de la matriz y se convierten a números todos aquellos que puedan ser convertidos, incluidas [las expresiones](README.md#representar-números). Se añade la matriz.
   2. Se añade el tipo de la matriz:
      - Tipo 0: Matriz cuadrada sin incógnitas.
      - Tipo 1: Matriz regular sin incógnitas.
      - Tipo 2: Matriz con incógnitas.
      - Tipo 3: Matriz irregular.
   3. Si la matriz es regular (sea cuadrada o no):
      1. Añade su número de filas.
      2. Añade su número de columnas, es decir, el número de elementos en cada fila.
      3. Añade [su rango](#cálculo-del-rango).
      4. Añade su matriz transpuesta.
      5. Si es cuadrada:
         1. Añade [la matriz identidad de orden n](#generar-matrices-identidad-de-orden-n) que le corresponde a la matriz.
         2. Dependiendo del rango de la matriz:
            1. Si es igual al número de filas:
               1. La matriz es invertible.
               2. Se inverte la matriz por el algoritmo de Gauss.
                  1. [Se escalona la matriz](#algoritmo-de-la-matriz-escalonada) y se guardan las operaciones realizadas en [la tabla de operaciones](#la-tabla-de-operaciones).
                  2. [Se calcula el determinante](#cálculo-del-determinante) y se añade.
                  3. [Se transforma la matriz escalonada en la matriz identidad](#transformar-la-matriz-escalonada-en-la-matriz-identidad) y se guardan las operaciones en la tabla.
               4. Se obtiene la matriz inversa [aplicando las operacions guardadas en la tabla a la matriz identidad](#inversión-de-matrices) y se añade.
               5. Se añade la tabla de operaciones.
            2. Si es menor que el número de filas:
               1. Se añade el determinante de la matriz, que es 0.
                  - Como el determinante es 0, la matriz no es invertible por lo que no se hace nada más.
4. Se exporta la lista de propiedades de cada matriz al archivo de salida:
   1. Se escribe el un título que contiene el índice de la matriz.
   2. Se escribe la matriz en [el estilo](README.md#opción-style-supmsup) elegido por el usuario.
   3. Dependiendo del segundo elemento de la lista, es decir, el tipo de parámetro:
      1. Si es 2 o 3:
         - Significa que la matriz es una matriz con incógnitas (2) o una matriz irregular (3).
         - Se indica el tipo de parámetro que es.
      2. Si es 0 o 1:
         - Significa que la matriz es una matriz regular, sea cuadrada (0) o no (1).
      3. Si la [opción 'dimensions'](README.md#otras-opciones-supmsup) está activada:
         1. Se escribe el número de filas de la matriz.
         2. Se escribe el número de columnas de la matriz.
      4. Si la [opción 'rank'](README.md#otras-opciones-supmsup) está activada:
         - Se escribe el rango de la matriz.
      5. Si la [opción 'transpose'](README.md#otras-opciones-supmsup) está activada:
         - Se escribe la matriz transpuesta en el estilo elegido por el usuario.
      6. Si la matriz es cuadrada:
         1. Si la [opción 'idmatrix'](README.md#otras-opciones-supmsup) está activada:
            - Se escribe la matriz identidad de orden n asociada a la matriz en el estilo elegido por el usuario.
         2. Si la [opción 'determinant'](README.md#otras-opciones-supmsup) está activada:
            - Se escribe la el determinante de la matriz.
         3. Si la matriz es invertible:
            1. Se escribe la matriz inversa en el estilo elegido por el usuario.
            2. Si la [opción 'oplist'](README.md#otras-opciones-supmsup) está activada:
               - Se escribe la lista de operaciones que se deben realizar para transformar la matriz identidad en la matriz inversa.

## Funcionamiento del modo ecuacional

1. Se lee [el archivo de entrada](README.md#opción-path-supmsup) y cada línea de [los sistemas de ecuaciones](README.md##sistemas-de-ecuaciones-lineales), que corresponde a una ecuación lineal, se procesa y se añade a su entrada en la lista de sistemas de ecuaciones lineales. Esta lista es un array tetradimensional que actúa como si fuese una matriz fila de matrices fila de dos elementos en las que el primer elemento es la lista de incógnitas del sistema de ecuaciones y el segundo elemento es [la matriz aumentada que representa el sistema de ecuaciones pero transpuesta](#los-sistemas-de-ecuaciones-lineales-en-este-programa).
2. Una vez procesados los sistemas lineales, se añade un número igual de entradas vacías a la lista de soluciones de los sistemas.
3. Se analiza cada sistema de ecuaciones y se rellena la lista de soluciones:
   1. Se obtienen la matriz de coeficientes y la matriz aumentada del sistema:
      1. La matriz de coeficientes consta de todas las filas de la matriz transpuesta excepto la última, la fila de las constantes.
         - Se transpone la matriz obtenida para obtener la matriz de coeficientes.
      2. La matriz aumentada consta de todas las filas de la matriz transpuesta.
         - Se transpone la matriz obtenida para obtener la matriz aumentada.
   2. Se compara el rango de la matriz de coeficientes y la matriz aumentada.
      1. Si el rango de la matriz de coeficientes es inferior al de la matriz aumentada:
         - El sistema es incompatible y se rellena la primera entrada de la lista de soluciones con su tipo: el tipo 0.
      2. Si el rango de la matriz de coeficientes es igual que el de la matriz aumentada:
         1. Si el número de incógnitas del sistema de ecuaciones es mayor que el rango:
            - El sistema es compatile indeterminado y se rellena la primera entrada de la lista de soluciones con su tipo: el tipo 1.
         2. Si el número de incógnitas del sistema de ecuaciones es igual que el rango:
            1. El sistema es compatible determinado y se rellena la primera entrada de la lista de soluciones con su tipo: el tipo 2.
            2. Se resuelve el sistema de ecuaciones mediante el algoritmo de Gauss-Jordan.
               2. Se escalona la matriz aumentada.
                  - Se comprueba si hay alguna fila nula en la matriz aumentada y se eliminan.
               3. Se convierte la matriz aumentada escalonada en una matriz escalonada reducida.
                  - Todas las columnas menos la última formarán una matriz identidad.
                  - La última columna la formarán los valores de las incógnitas.
            3. Se transpone la matriz resultante.
            4. Se añade a la lista de soluciones la lista de parámetros del sistema.
            5. Se añade a la lista de soluciones la última fila de la matriz transpuesta: la fila que contiene el valor de cada incógnita.
4. Se exporta la lista de soluciones de cada sistema de ecuaciones al archivo de salida:
   1. Se escribe un título que contiene el índice del sistema de ecuaciones.
   2. Se escribe el sistema de ecuaciones.
   3. Se observa el primer elemento de la lista de soluciones (el tipo de sistema) y se escribe.
   4. Según el tipo de sistema:
      1. Si el sistema es incompatible o compatible indeterminado:
         - No se hace nada más.
      2. Si el sistema es compatible determinado:
         - Se escribe una lista con los valores de cada incógnita.

## Algoritmos

### Algoritmo de la matriz escalonada

La función encargada de convertir matrices en matrices escalonadas (matrices triangulares superiores) es la función rowEchelonMatrix.

Esta función recibe cuatro argumentos:

- [Una matriz](#las-matrices-en-este-programa)
- Un valor resultante del producto de los valores entre los que se dividen las filas para dividirlas entre su pivote (el factor)
- El número de veces que se ha realizado la operación de intercambio de filas hasta el momento
- [La tabla de operaciones](#la-tabla-de-operaciones)

El proceso de escalonar una matriz es el siguiente:

1. [Se ordenan las filas de la matriz](#ordenamiento-de-filas).
2. Se actualizan:
   - El contador de veces que se han realizado intercambios de filas
   - La tabla de operaciones.
3. Se divide la primera fila entre su pivote.
   1. Se actualiza el registro de operaciones.
   2. Se multiplica el factor por el pivote.
4. Por cada fila de la matriz (filas 1):
   - Se iteran las filas que tienen un índice inferior (filas 2):
      - Si la fila no es nula (todos los elementos son 0):
         1. Se escalona la fila 1:
            - La función encargada de este proceso es la función rowEchelonRow.
            1. Se obtiene el índice del pivote de la fila 2, cuya posición coincide con el número de ceros de la fila (a no ser que la fila sea nula) ya que las filas son listas con índice 0.
            2. Se obtiene un factor resultante de la división entre el elemento j de la fila 2 (su pivote) y el elemento j de la fila 1.
            3. Se resta la fila 2 multiplicada por el factor a la fila 1.
               - Por cómo trata Python los números flotantes, hay que comprobar que algunos elementos que son números flotantes muy pequeños no sean en realidad ceros.
                  - Para más información visita la función substractRows en el código.
            4. Se actualiza el registro de operaciones.
5. Se comprueba si la matriz resultante es una matriz escalonada o no.
   - La encargada de esta comprobación es la función checkIfRowEchelon.
   - Para que la matriz esté escalonada tiene que haber una progresión en el número de ceros que hay a la izquierda del pivote de cada fila.
      - De hecho, se llama escalonada porque los ceros a la izquierda de los pivotes forman una especie de escalón.
   1. Si lo es:
      - Devuelve la matriz, el factor, el contador de intercambios de filas y la tabla de operaciones.
   2. Si no lo es:
      - La función se vuelve a llamar a sí misma para seguir escalonando la matriz; dando como argumentos la matriz en proceso de escalonación, el factor actual, el número de veces que se han intercambiado filas hasta ese momento y el estado actual de la tabla de operaciones.

### Ordenamiento de filas

La función encargada de realizar el proceso de ordenar las filas en función de los ceros a la izquierda del pivote e intercambiar la fila 1 por la fila cuyo primer elemento tenga el valor absoluto más grande es la función orderRows.

El proceso es el siguiente:

1. Se ordenan las filas según el número de ceros a la izquierda del pivote.
   1. Se iteran las filas 1 en función del número de filas de la matriz.
      - Se hace lo mismo con las filas 2.
         - Si el índice de la fila 1 es mayor que el de la fila 2:
            1. Se cuentan los ceros a la izquierda del pivote de la fila 1.
            2. Se cuentan los ceros a la izquierda del pivote de la fila 2.
            3. Si el número de elementos nulos a la izquierda del pivote en la fila 1 es mayor que en la fila 2:
               1. Se intercambian la fila 1 y la fila 2.
               2. Se incrementa en 1 el contador de veces que se han realizado intercambios de filas en 1.
               3. Se actualiza el registro de operaciones con el intercambio realizado.
2. Se intercambia la fila 1 por la fila cuyo primer elemento tenga un valor absoluto mayor.
   - La función encargada de devolver el índice de la fila con el primer elemento con un valor absoluto más grande es la función biggestRow.
   - Esto se hace porque es más eficiente dividir una vez entre un valor grande que restar muchas veces multiplicando por un valor grande.
   - La verdad es que he implementado este paso porque a la hora de comprobar los resultados he visto que WolframAlpha lo hacía.
   1. Se obtiene el índice de la fila con el primer elemento más grande.
   2. Si la fila con el valor absoluto más grande no es la primera:
      1. Se intercambia la fila más grande con la primera fila.
      2. Se incrementa en 1 el contador de veces que se han realizado intercambios de filas en 1.
      3. Se actualiza el registro de operaciones con el intercambio realizado.
3. Se devuelven la matriz con las filas ordenadas, el número de veces que se ha realizado la operación de intercambio de filas en el proceso de ordenar la matriz y el registro de operaciones actualizado.

### Cálculo del rango

La función matrixRank es la encargada del cálculo del rango de una matriz. Esta función tiene necesita que se le pase una matriz como argumento y devuelve el rango de ésta.

Como el rango de una matriz equivalente X es el mismo que el de una matriz original A, el proceso del cálculo del rango de una matriz es el siguiente:

1. [Se crea una matriz escalonada](#algoritmo-de-la-matriz-escalonada).
   1. Se introducen la matriz, 1, 0 y una lista vacía como argumento de la función rowEchelonMatrix.
      - Como no se van a calcular ni el determinante ni la matriz inversa, no se necesita mantener un registro de los factores, intercambios de filas y operaciones realizadas. Es por esto que las 3 últimas entradas son triviales.
   2. Se asigna la primera salida (la matriz escalonada) de la función rowEchelonMatrix a una nueva matriz equivalente.
2. Se establece un contador de las filas nulas (aquellas en las que todos los elementos son 0).
3. Por cada fila de la matriz:
   - Si la fila es nula:
      - Se incrementa el contador de filas nulas en 1.
4. El rango es el valor resultante de la resta entre el número de filas de la matriz y el número de filas nulas.

### Cálculo del determinante

Realmente, el determinante solo necesita ser calculado si el rango de una matriz cuadrada es igual a su número de filas. En caso contrario, es 0.

Es por eso que antes de calcular el determinante el programa hace esta comprobación.

La función encargada de calcular el determinante es la función calculateDeterminant, que necesita tres entradas:

- [Una matriz escalonada](#algoritmo-de-la-matriz-escalonada)
- El factor por el que se va a multiplicar el determinante y que es resultado de el produto de las constantes por las que se han dividido las filas para dividirlas entre su pivote.
- El número de veces que se ha realizado la operación de intercambio de filas.

El proceso del cálculo del determinante es el siguiente:

1. Se le da al determinante un valor inicial de 1, ya que 1 es el elemento neutro de la multiplicación.
2. Se multiplica el determinante por el producto de los elementos de la diagonal, para ello:
   - Por cada fila en la matriz:
      - Por cada elemento:
         - Si el elemento comparte índice con su fila:
            - Se multiplica el valor actual del determinante por el elemento.
3. Se multiplica el determinante por el factor.
4. Si el número de veces que se ha realizado la operación de intercambio de filas es impar:
   - Se cambia el signo del determinante.

Aunque quizá no lo parezca a partir de esta explicación, el algoritmo del cálculo del determinante es recursivo ya que aprovecha la función rowEchelonMatrix que sí es recursiva.

### Transposición de matrices

La función transposeMatrix se encarga de la transposición de matrices.

Esta función requiere tres parámetros de entrada:

1. [La matriz](#las-matrices-en-este-programa)
2. El número de filas de la matriz (la dimensión 1)
   - Es la longitud de la lista que representa la primera dimensión del arreglo.
3. El número de columnas de la matriz (la dimensión 2)
   - Es la longitud de la lista que representa la segunda dimensión del arreglo (una fila). Como las matrices que se transponen en este programa son matrices regulares, basta con aportar el número de elemenos de la primera fila.

El proceso de transposición de las matrices es el siguiente:

1. Se declara una lista vacía que será la matriz transpuesta.
2. Por cada columna de la matriz original:
   1. Se añade una nueva fila vacía a la matriz transpuesta.
   2. Por fila en la matriz original:
      - Se añade un 0 a la fila de la matriz transpuesta.
   3. Por cada fila de la matriz original:
      - Por cada elemento de la fila:
         - Se establece que el elemento [j] [i] de la matriz transpuesta es el elemento [i] [j] de la matriz original.

### Generar matrices identidad de orden n

La función identityMatrix se encarga de generar matrices identidad de orden n, siendo n un número entero positivo que se le ha pasado a la función como argumento.

El proceso de generación de matrices identidad es el siguiente:

1. Se declara una lista vacía que servirá como la matriz identidad.
2. Por cada fila de 0 a n:
   1. Se añade una fila vacía.
   2. Por cada elemento de 0 a n:
      1. Si el elemento comparte índice con la fila:
         - Se añade un 1 a la fila.
      2. Si el elemento no comparte índice con la fila:
         - Se añade un 0 a la fila.

### Transformar la matriz escalonada en la matriz identidad

La función encargada de transformar las matrices escalonadas en matrices identidad es la función rowEchelonToIdentityMatrix.

También sirve para transformar matrices no cuadradas en matrices escalonadas reducidas que contienen las soluciones de los sistemas de ecuaciones lineales compatibles determinados.

El proceso para convertir una matriz escalonada en una matriz escalonada reducida o matriz identidad es el siguiente:

1. Se introduce [una matriz escalonada](#algoritmo-de-la-matriz-escalonada).
2. Por cada fila:
   - Se divide la fila por su pivote.
      - Se actualiza el registro de operaciones.
3. Se declara una constante de iteración:
   - Por cada iteración:
      1. Se define la fila 2, la fila que se restará a la otra fila (la fila 1) como el número de filas de la matriz menos la constante de iteración (ajustado a índice 0, es decir, - 1).
      2. Por cada fila uno desde la primera hasta la fila 2 (ajustado a índice 0):
         1. Se define un factor que es el resultado de dividir el elemento j de la fila 1 entre el elemento j de la fila 2, es decir, el pivote de la fila 2.
         2. Si la fila 2 tiene un índice mayor que el de la fila 1 y el factor no es 0 (para no multiplicar por 0 porque multiplicar por 0 y sumar o restar es lo mismo que no hacer nada):
            1. Se resta la fila 2 multiplicada por el factor a la fila 1.
            2. Se actualiza el registro de operaciones.

La función devuelve dos variables: la tabla de operaciones y la matriz resultante. El modo matricial aprovecha la primera salida para invertir las matrices mientras el modo ecuacional aprovecha la segunda salida para resolver los sistemas de ecuaciones.

### Inversión de matrices (algoritmo de Gauss)

En este programa la inversión de matrices cuadradas se lleva a cabo mediante el algoritmo de Gauss.

Si bien gran parte del proceso de inversión de matrices se lleva a cabo dentro de la función matrixProperties comparte el rol de ser la encarga de la inversión de matrices con la función invertMatrix.

El proceso de inversión de matrices es el siguiente:

1. Se comprueba si el rango de la matriz es igual a su número de filas.
   1. Si no lo es:
      - La matriz no es invertible.
   2. Si lo es:
      1. Se escalona la matriz.
         - Se guarda un registro de las operaciones que se han necesitado para escalonar la matriz.
      2. [Se convierte la matriz escalonada en la matriz identidad](#transformar-la-matriz-escalonada-en-la-matriz-identidad).
         - Se guarda un registro de las operaciones que se han necesitado para hacerlo, que es la primera salida de la función rowEchelonToIdentityMatrix.
      3. Se aplican las operaciones guardas en el registro de operaciones a la matriz identidad de orden n asociada a la matriz.

## Operaciones elementales de filas

|                 Operación                |      Función     | Código |
|:----------------------------------------:|:----------------:|:------:|
| Multiplicar y dividir fila por constante |  multiplyRow ()  |    0   |
|            Intercambiar filas            |    swapRows ()   |    1   |
|           Restar y sumar filas           | substractRows () |    2   |

### Multiplicar y dividir fila por constante

La función encargada de multiplicar y dividir filas por constantes es la función multiplyRow. Esta función recoge una fila y un factor como argumentos y devuelve la fila después de dividirla por el factor.

Para ello:

1. Se crea una lista vacía que servirá como la nueva fila.
2. Por cada elemento de la fila original:
   1. Se divide entre el factor.
   2. Se añade a la nueva fila.

### Intercambiar filas

La función encargada de dividir filas es la función swapRows. Esta función recoge como argumentos una matriz y dos filas y devuelve la matriz con las filas intercambiadas.

Para ello:

1. Se crea una nueva fila 1 igual a la fila 2 original.
2. Se crea una nueva fila 2 igual a la fila 1 original.
3. Se sustituye la fila 1 de la matriz por la nueva fila 1.
4. Se sustituye la fila 2 de la matriz por la nueva fila 2.

### Restar y sumar filas

La función encargada de restar y sumar filas es la función substractRows. Esta función recoge dos filas y un factor como argumentos y devuelve la nueva fila 1, que es el resultado de restar la fila 2 multiplicada por el factor a la fila 1.

Para ello:

1. Se crea una lista vacía que servirá como la nueva fila 1.
2. Por cada elemento en la fila 1:
   1. Se realiza la resta entre el elemento j de la fila 1 y el elemento j de la fila 2 multiplicado por el factor.
   2. Se añade el elemento resultante a la nueva fila 1.

Esta función también hace sumas ya que si el factor es negativo las restas se convierten en restas de números negativos, es decir, sumas.

## Propiedades de las matrices

Esta es una representación de cada conjunto de propiedades de cada matriz introducida por el usuario en la lista, donde cada fila de la tabla comparte posición en la lista de propiedades. Por ese motivo, podríamos decir que la lista de listas de propiedades de las matrices (la variable *propertyList*) es parecida a una matriz fila de matrices fila en la que los elementos son los siguientes:

|               Propiedad              |                              Valores posibles                              |
|:------------------------------------:|:--------------------------------------------------------------------------:|
|                Matriz                |        Una de las matrices introducidos por el usuario en el archivo       |
|          Tipo de parámetro           |                                 0, 1, 2 o 3                                |
|    Número de filas (m)<sup>R</sup>   |                               Entero positivo                              |
|  Número de columnas (n)<sup>R</sup>  |                               Entero positivo                              |
|          Rango<sup>R</sup>           |                               Entero positivo                              |
|    Matriz transpuesta<sup>R</sup>    |                          Matriz de m×n dimensiones                         |
|     Matriz identidad<sup>C</sup>     |                         Matriz identidad de orden n                        |
|       Determinante<sup>C</sup>       |                               Número flotante                              |
|      Matriz inversa<sup>C</sup>      |                              Matriz de orden n                             |
|   Tabla de operaciones<sup>C</sup>   |   Matriz irregular con las operaciones a realizar para invertir la matriz  |

**\*** <sup>R</sup> = Presente solo si la matriz es una matriz regular sin incógnitas.

**\*\*** <sup>C</sup> = Presente solo si la matriz es una matriz cuadrada sin incógnitas.

## Propiedades de los sistemas de ecuaciones

La variable *solutionList* es el análogo de los sistemas de ecuaciones de la variable *propertyList* de las matrices.

Esta es una representación de la lista en forma de tabla:

|                   Propiedad                  |   Valores posibles  |
|:--------------------------------------------:|:-------------------:|
|         Tipo de sistema de ecuaciones        |       0, 1 o 2      |
| Lista de incógnitas del sistema<sup>CD</sup> | Lista de carácteres |
|    Valores de las incógnitas<sup>CD</sup>    |   Lista de números  |

**\*** <sup>CD</sup> = Presente solo si el sistema de ecuaciones lineales es un sistema compatible determinado.
