# -----------------------------------------------------
# |                    SimpleGauss                    |
# |                                                   |
# | Analizador de matrices y solucionador de sistemas |
# |                                                   |
# |     Proyecto dual de Programación I y Álgebra     |
# |                                                   |
# |           Autor: Mikel Pintado del Campo          |
# -----------------------------------------------------


# Esta variable establece la versión del programa a utilizar.
# Para utilizar la versión estándar o versión 0 (la que recomiendo usar), hay que establecer el valor de la variable en 0.
# Para utilizar la versión Prog o versión 1, hay que establecer el valor de la variable en 1.
version = 1

# Configuración del programa para la versión estándar.
# 
# Esta es una configuración de ejemplo que he aprovechado para comentar.
# Puede crearse una configuración con la combinación que se quiera de las 12 opciones disponibles. Incluso puede no haber alguna de ellas o ninguna.
# Para más información sobre las opciones y el funcionamiento del programa, visita la documentación.
config = {
    # Opción 'mode'
    #
    # Establece el modo en el que opera el programa.
    
    # Puede tomar dos valores, uno por cada modo del programa:
    # - 0: El programa opera en modo matricial.
    # - 1: El programa opera en modo ecuacional.
    
    # Si no se especifica un valor para la opción mode, su valor será 0. Esto quiere decir que el modo por defecto del programa será el modo matricial.
    'mode': 1,

    # Opción 'path'
    #
    # La ruta del archivo de la que se sacan las matrices y sistemas de ecuaciones lineales.
    # El archivo de entrada deberá tener la extensión .input y el archivo de salida compartirá nombre y ruta pero
    # contará con la extensión .output.
    #
    # Por ejemplo, para que el resultado sea el siguiente:
    # - Ruta del archivo de entrada: C:/Users/mikel/Documents/algo.input
    # - Ruta del archivo de salida: C:/Users/mikel/Documents/algo.output
    #
    # La opción 'path' deberá ser ajustada de la siguiente forma:
    # 'path': 'C:/Users/mikel/Documents/algo'
    #
    # También funciona con rutas relativas ya que el funcionamiento es el mismo.
    #
    # Si por algún motivo la opción 'path' no ha sido especificada, el archivo de salida se encontrará en la carpeta del programa
    # y su nombre será la fecha y hora del día en el que se ha generado. Por ejemplo, si el programa se encuentra en la carpeta
    # /home/mikel/Descargas y son las 11:52:17 pm del 21/02/2022, el archivo de salida será /home/mikel/Descargas/22-02-21_23-52-17.output.
    #
    # Si se cumple el caso anterior y la opción 'random' está activada (>0), se operará con la matriz generada.
    # Si está desactivada (=0 o no definida), en cambio, se operará con la matriz identidad de orden 3 (cuya inversa es la misma matriz identidad de orden 3).
    'path': 'examples/eqsys/example',

    # Las opciones que se encuentran a partir de aquí son exclusivas del modo matricial.
    # Aún así, estas opciones deben estar bien definidas incluso si el usuario está operando en modo ecuacional.

    # Opción 'random'
    #
    # Operar con matrices cuadradas aleatorias en vez de matrices ya incluidas en un archivo.
    # Esta opción tiene preferencia sobre los archivos de entrada en caso de estar activada.
    #
    # El comportamiento por defecto de esta opción será estar desactivada, es decor. tener 0 como valor.
    # Para activarla, hay que introducir un número natural superior a 0 que indique el orden de la matriz cuadrada a generar.
    'random': 5,

    # Opción 'random.number'
    #
    # Establece el número de matrices cuadradas aleatorias a generar en caso de que la opción 'random' esté activada.
    #
    # El valor que esta opción tomará por defecto es 1.
    'random.number': 10,

    # Opción 'random.rank'
    #
    # Rango de valores con los que las matrices aleatorias serán rellenadas. Estos valores pertenecerán al conjunto de los números enteros
    # y serán aquellos que se encuentren entre -n y n (incluidos).
    #
    # El valor por defecto de esta opción es 9, para que se generen matrices aleatorias 
    # cuyos elementos solo tomen como valores los dígitos del sistema decimal y sus análogos negativos.
    'random.rank': 100,

    # Opción 'style'
    # 
    # El estilo al que se exportarán las matrices.
    #
    # Estilos:

    # 1, py, python o plain
    # -> Exporta la matriz como array bidimensional de Python. Puede ser útil si se quiere introducir las matrices en otro programa similar hecho en Python.
    # 2, wa, wolfram
    # -> Exporta la matriz al formato de Wolfram Mathematica (y Wolfram Alpha). Es útil para comprobar los resultados en el kernel de Wolfram Mathematica.
    # 3, default o human
    # -> Exporta la matriz a un formato más legible, parecido al de las matrices que pueden verse en un libro de matemáticas.
    'style': 'wa',

    # Otras opciones:
    #
    # Establecen la información sobre la matriz que se mostrará en el archivo de salida.
    #
    # Estos son parámetros opcionales, ya que el programa siempre mandará la matriz inversa al archivo de salida
    # Para que un parámetro esté presente, hay que establecerlo su valor en 1. En cambio, para que no esté presente basta
    # con establecerlo su valor en 0 o no definir la opción correspondiente,
    # pues el comportamiento por defecto de estas opciones es no estar presentes.
    #
    # Lista de opciones:
    # - rank -> Muestra el rango de la matriz introducida.
    # - dimensions -> Muestra las dimensiones de la matriz introducida.
    # - transpose -> Muestra la matriz transpuesta de la matriz introducida, siempre y cuando esta sea cuadrada.
    # - determinant -> Muestra el determinante de la matriz introducida.
    # - idmatrix -> Muestra la matriz identidad de orden n asociada a la matriz cuadrada introducida.
    # - oplist -> Muestra una lista con las operaciones que se han realizado para invertir la matriz.
    'rank': 1,
    'dimensions': 1,
    'transpose': 1,
    'determinant': 1,
    'idmatrix': 1,
    'oplist': 1
}

# Módulos de Python a importar:

# Módulo sys
# Para hacer que el programa tenga códigos de salida.
import sys

# Módulo os
# Para hacer que el programa pueda leer el sistema de archivos del sistema operativo que está ejecutando el programa además de ejecutar comandos del sistema.
import os

# Módulo random
# Para generar números aleatorios en caso de que se quieran generar matrices aleatorias.
import random

# Módulo datetime
# Para conseguir la fecha y hora en la que está ejecutándose el programa.
from datetime import datetime

# Módulo math
# Para realizar operaciones matemáticas como quitar la parte decimal de números decimales.
import math

# A partir de aquí, se definen las funciones del programa. Para ver la parte principal del programa hay que ir al final del código.

# Función testConfig
# Realiza una comprobación de la configuración del programa proporcionada por el usuario para comprobar que todos los parámetros cumplen
# con los criterios para ser correctos además de añadir aquellos que no existen con sus valores por defecto.
def testConfig (config):
    # Declara una lista con el conjunto de parámetros que puede tener la configuración del programa. Cada parámetro será una llave.
    keyList = ['mode', 'path', 'random', 'random.number', 'random.rank', 'style', 'rank', 'dimensions', 'transpose', 'determinant', 'idmatrix', 'oplist']

    # Declara una lista con los nombres de los estilos a los que se pueden exportar las matrices.
    styleList = ['py', 'python', 'plain', 'wa', 'wolfram', 'default', 'human', '1', '2', '3']

    # Inicializa un diccionario que servirá como la configuración después del testeo.
    newConfig = {}

    # Se añaden las llaves especificadas en la lista de llaves y a cada una se le da un valor nulo.
    for key in keyList:
        newConfig [key] = None

    # Se analiza cada llave de la configuración proporcionada por el usuario y se mira si cumple con los requisitos para ser un parámetro válido según su valor.
    # Si no es válido, se sale del programa con el código de error de cada fallo de configuración, proporcionando al usuario un mensaje de error.
    # Ademas, si no existe el parámetro en la configuración original,
    # se añade a la nueva configuración con el valor por defecto especificado en la descripción de la configuración.

    # La opción 'mode' se analiza la primera para ver si la opción 'path' especificada es válida.

    # Se establece que la opción a analizar es 'mode'.
    key = 'mode'

    # Si está definida:
    if (key in config):
        # Si no es 0 o 1:
        if (config [key] != 0 and config [key] != 1):
            # Se indica que hay un error en la configuración y se sale del programa con el código de error 3.
            print ('La opción \"mode\" debe tomar como valor 0 o 1.')
            sys.exit (3)

        # Si está bien definida:
        else:
            # Se añade a la nueva configuración.
            newConfig [key] = config [key]

    # Si no está definida:
    else:
        # Se le da su valor por defecto: 0.
        newConfig [key] = 0

    for key in keyList:
        # Para la opción 'path'.
        if (key == 'path'):
            # Si está definida:
            if (key in config):
                # Si el valor no es una cadena de carácteres:
                if (type (config [key]) != str):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 4.
                    print ('La opción \"path\" debe ser una cadena de carácteres que equivalga a la ruta de un archivo.')
                    sys.exit (4)

                # Si el valor es una cadena de carácteres vacía:
                elif (config [key] == ''):
                    # Limpia la pantalla.
                    clearScreen ()

                    # Sale del programa con el código de error 0.
                    # Esto es útil en la versión 1, en la que se da al usuario la opción de salir del programa pulsando Enter.
                    sys.exit (0)

                # Si el valor es una cadena de carácteres que no esté vacía:
                else:
                    # Se saca el directorio de la ruta especificada en la variable.
                    dir = os.path.dirname (config [key])

                    # Si el archivo está en la misma ruta que el programa:
                    if (dir == ''):
                        # Se establece el directorio como '.', es decir, el mismo del programa.
                        dir = '.'

                    # Si la ruta especificada no existe:
                    if (not os.path.exists (dir)):
                        # Se crea y se da un aviso. No se sale del programa porque al usuario puede interesarle seguir si está operando con matrices aleatorias.
                        os.makedirs (dir)
                        print (f'La ruta especificada en la opción \'path\', {config [key]}, no existe.\nTen en cuenta que el programa no funcionará si opción \'random\' está desactivada.')

                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]

            # Si la opción 'path' no está definida y el programa está en modo matricial (modo 0):
            elif (key not in config and newConfig ['mode'] == 0):
                # Se le da su valor por defecto: la fecha y hora de ejecución del programa.
                newConfig [key] = executionDate

            # La opción 'path' es la excepción: si el programa está en modo ecuacional (modo 1) no puede tomar un valor por defecto,
            # tiene que ser un archivo existente especificado por el usuario.
            # A no ser que la ruta especificada sea 'NoInputYet', que está reservada para omitir el testeo de 'path' en el modo ecuacional
            # hasta que no se le haya preguntado al usuario la ruta que desea introducir.
            if (newConfig ['mode'] == 1 and config [key] != 'NoInputYet' and (key not in config or not os.path.exists (config [key] + '.input'))):
                # Genera un mensaje de error y sale del programa con el código de error 5.
                print ('La opción \"path\" debe especificar un archivo de entrada que exista si el programa está en modo ecuacional.')
                sys.exit (5)

        # Para la opción 'random'.
        elif (key == 'random'):
            # Si está definida:
            if (key in config):
                # Si no es un entero o es menor que 0.
                if (type (config [key]) != int or config [key] < 0):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 6.
                    print ('La opción \"random\" debe tomar como valor un número entero que sea igual o mayor que 0.')
                    sys.exit (6)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]

            # Si no está definida:
            else:
                # Se le da su valor por defecto: 0.
                newConfig [key] = 0

        # Para la opción 'random.number'.
        elif (key == 'random.number'):
            if (key in config):
                if (type (config [key]) != int or config [key] < 1):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 7.
                    print ('La opción \"random.number\" debe tomar como valor un número entero que sea igual o mayor que 1.')
                    sys.exit (7)

                else:
                    newConfig [key] = config [key]

            else:
                newConfig [key] = 1

        # Para la opción 'random.rank'.
        elif (key == 'random.rank'):
            # Si está definida:
            if (key in config):
                # Si no es un entero o es menor o igual a 0:
                if (type (config [key]) != int or config [key] <= 0):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 8.
                    print ('La opción \"random.rank\" debe tomar como valor un número entero positivo.')
                    sys.exit (8)

                # Si está bien definida:
                else:
                    newConfig [key] = config [key]

            else:
                # Se le da su valor por defecto: 9.
                newConfig [key] = 9

        # Para la opción 'style'.
        elif (key == 'style'):
            # Si está definida:
            if (key in config):
                # Si el valor especificado (convertido a string para que no importe introducir '1' o 1) no es un estilo válido:
                if (str (config [key]) not in styleList):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 9.
                    print ('La opción \"style\" debe ser una de las siguientes: \"1\", \"py\", \"python\", \"plain\", \"2\", \"wa\", \"wolfram\", \"3\", \"default\" o \"human\".')
                    sys.exit (9)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = str (config [key])

            # Si no está definida:
            else:
                # Se le da su valor por defecto: 'default'.
                newConfig [key] = 'default'

        # Para la opción 'rank'.
        elif (key == 'rank'):
            # Si está definida:
            if (key in config):
                # Si no es 0 o 1:
                if (config [key] != 0 and config [key] != 1):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 10.
                    print ('La opción \"rank\" debe tomar como valor 0 o 1.')
                    sys.exit (10)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]

            # Si no está definida:
            else:
                # Se le da su valor por defecto: 0.
                newConfig [key] = 0

        # Para la opción 'dimensions'.
        elif (key == 'dimensions'):
            # Si está definida:
            if (key in config):
                # Si no es 0 o 1:
                if (config [key] != 0 and config [key] != 1):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 11.
                    print ('La opción \"dimensions\" debe tomar como valor 0 o 1.')
                    sys.exit (11)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]

            # Si no está definida:
            else:
                # Se le da su valor por defecto: 0.
                newConfig [key] = 0

        # Para la opción 'transpose'.
        elif (key == 'transpose'):
            # Si está definida:
            if (key in config):
                # Si no es 0 o 1:
                if (config [key] != 0 and config [key] != 1):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 12.
                    print ('La opción \"transpose\" debe tomar como valor 0 o 1.')
                    sys.exit (12)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]


            # Si no está definida:
            else:
                # Se le da su valor por defecto: 0.
                newConfig [key] = 0

        # Para la opción 'determinant'.
        elif (key == 'determinant'):
            # Si está definida:
            if (key in config):
                # Si no es 0 o 1:
                if (config [key] != 0 and config [key] != 1):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 13.
                    print ('La opción \"determinant\" debe tomar como valor 0 o 1.')
                    sys.exit (13)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]


            # Si no está definida:
            else:
                # Se le da su valor por defecto: 0.
                newConfig [key] = 0

        # Para la opción 'idmatrix'.
        elif (key == 'idmatrix'):
            # Si está definida:
            if (key in config):
                # Si no es 0 o 1:
                if (config [key] != 0 and config [key] != 1):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 14.
                    print ('La opción \"idmatrix\" debe tomar como valor 0 o 1.')
                    sys.exit (14)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]

            # Si no está definida:
            else:
                # Se le da su valor por defecto: 0.
                newConfig [key] = 0

        # Para la opción 'oplist'.
        elif (key == 'oplist'):
            # Si está definida:
            if (key in config):
                # Si no es 0 o 1:
                if (config [key] != 0 and config [key] != 1):
                    # Se indica que hay un error en la configuración y se sale del programa con el código de error 15.
                    print ('La opción \"oplist\" debe tomar como valor 0 o 1.')
                    sys.exit (15)

                # Si está bien definida:
                else:
                    # Se añade a la nueva configuración.
                    newConfig [key] = config [key]

            # Si no está definida:
            else:
                # Se le da su valor por defecto: 0.
                newConfig [key] = 0

    # Devuelve la nueva configuración si es que los parámetros que existían en la anterior configuración eran válidos.
    # Además, también se le ha asignado un valor a aquellos parametros que no existían previamente.
    return newConfig

# Función randomMatrix
# Genera una matriz cuyos valores son números enteros aleatorios dentro de un intervalo [-n, n].
# La matriz será una matriz cuadrada de orden m, donde m es un entero superior a 0 especificado en la opción 'random' de la configuración.
def randomMatrix (dimension):
    # Inicializa la matriz como un array vacío.
    matrix = []

    # Se crea una matriz cuadrada de la siguiente forma.
    for row in range (dimension):
        # Se añade el número de filas especificado en la opción 'random'.
        matrix.append ([])

        # Por cada fila se añade el número de elementos especificado en la opción 'random'.
        for rowe in range (dimension):
            # Cada elemento será un entero que se encuentre en el intervalo [-n, n]
            matrix [row].append (random.randint (-config ['random.rank'], config ['random.rank']))

    # Devuelve la matriz aleatoria generada.
    return matrix

# Función generateMatrixList
# Se genera la lista de matrices con las que se va a operar.
# Esta lista será un array tridimensional cuyas dimensiones actuarán como lo siguiente:
# - Primera dimensión: las matrices.
# - Segunda dimensión: las filas de las matrices.
# - Tercera dimensión: los elementos de las filas de las matrices.
# Además, se genera otra lista complementaria de propiedades de cada matriz.
# Será un array bidimensional en el que la primera dimensión será  el conjunto de propiedades de cada matriz y la segunda cada propiedad.
def generateMatrixList (path):
    # Se inicializa la lista de matrices como una lista vacía.
    matrixList = []

    # Se inicia la lista de propiedades de las matrices como una lista vacía.
    propertyList = []

    # Si la opción 'random' está activa, genera una lista de n matrices aleatorias (siendo n el valor de la opción 'random.number').
    if (config ['random'] > 0):
        for matrix in range (config ['random.number']):
            matrixList.append (randomMatrix (config ['random']))

    # Si la opción 'random' está desactivada:
    else:
        # Si el archivo de entrada existe:
        if (os.path.exists (path)):
            # Genera una lista de matrices con las matrices del archivo.
            matrixList = parseMatrixList (path)

        # Si el archivo de entrada no existe:
        else:
            # Genera una lista de matrices que solo contenga matrices identidad de orden 3, pero la cantidad de veces especificada en la opción 'random.number'.
            for matrix in range (config ['random.number']):
                matrixList.append (identityMatrix (3))

    # Si la lista de matrices está vacía, es decir, no se ha introducido ninguna matriz:
    if (matrixList == []):
        # Se añade la matriz identidad de orden 3.
        matrixList.append (identityMatrix (3))

    # Por cada matriz:
    for matrix in range (len (matrixList)):
        # Añade una entrada nueva a la lista de propiedades.
        propertyList.append ([])

    # Devuelve la lista de matrices y la lista de propiedades de las matrices.
    return matrixList, propertyList

# Función parseMatrixList
# Si el archivo de entrada existe, genera una lista de matrices con las matrices del archivo.
def parseMatrixList (path):
    # Se inicializa la lista de matrices como una lista vacía.
    matrixList = []

    # Abre el archivo de entrada en el que se encuentran las matrices a invertir.
    inputFile = open (path, 'r')

    # Se empieza por la primera fila de la primera matriz.
    matrix = 0
    row = 0

    # Se añade la primera matriz, que estará vacía.
    matrixList.append ([])

    # Analiza cada línea del archivo.
    for line in inputFile:
        # Si la línea es una línea vacía, pasa a la siguiente matriz.
        if (line in ['\n', '\r\n']):
            matrix += 1
            row = 0
            matrixList.append ([])

        # Si la línea tiene contenido:
        else:
            # Añade una nueva fila.
            matrixList [matrix].append ([])

            # Separa los elementos de la línea en función de los espacios.
            roweList = line.split (' ')

            # Se analiza cada elemento de la fila.
            for rowe in roweList:
                # Si el elemento contiene el carácter de salto de línea, se lo quita.
                # Esto pasa con el último elemento de cada fila.
                if ('\n' in rowe):
                    rowe = rowe.replace ('\n', '')

                # Si el elemento no está vacío (esto pasa cuando hay varios espacios seguidos):
                if (rowe != ''):
                    # Se añade a la fila.
                    matrixList [matrix] [row].append (rowe)

            # Una vez terminado el proceso, se salta de línea.
            row += 1

    # Cierra el archivo de entrada.
    inputFile.close ()

    # Antes de devolver la lista de matrices:

    # Se analiza cada matriz:
    for matrix in range (len (matrixList)):
        # Se filtran los elementos que tengan un valor nulo, es decir, las filas vacías.
        matrixList [matrix] = list (filter (None, matrixList [matrix]))

    # Se filtran aquellas matrices que estén vacías y se eliminan de la lista:
    matrixList = list (filter (None, matrixList))

    # Devuelve la lista de matrices.
    return matrixList

# Función inputMatrix
# Esta función permite al usuario introducir una matriz a través de inputs en vez de a través de un archivo.
# Se usa en la versión Prog en caso de que el usuario desee introducir matrices adicionales.
def inputMatrix ():
    # Se crea una lista vacía que contendrá las filas de la matriz tipadas como strings.
    rawMatrix = []

    # Se crea una matriz que por el momento estará vacía.
    matrix = []

    # Se pide al usuario que introduzca una fila hasta que pulse Enter.
    # Para ello, se simula otro bucle do-while.

    shouldRestart = True

    while (shouldRestart):
        # Se limpia la pantalla.
        clearScreen ()

        # Se pregunta al usuario que introduzca una fila.
        print (f'Introduce la fila {len (rawMatrix) + 1} [Enter para terminar]: ', end = '')
        row = input ()

        # Si la respuesta del usuario es un string vacío, es decir, ha pulsado Enter sin introducir nada:
        if (row == ''):
            # Se establece que el bucle no se repetirá.
            shouldRestart = False

        # En caso contrario:
        else:
            # Se añade la fila a la lista de filas.
            rawMatrix.append (row)

            # Se añade una nueva fila vacía a la matriz.
            matrix.append ([])

    # Se transforma cada fila de la matriz y se añade a la matriz:
    for row in range (len (rawMatrix)):
        # Se separan los elementos de la fila en función de los espacios.
        roweList = rawMatrix [row].split (' ')

        # Se analiza cada elemento de la fila.
        for rowe in roweList:
            # Si el elemento no está vacío (esto pasa cuando hay varios espacios seguidos):
            if (rowe != ''):
                # Se añade a la fila respectiva de la matriz.
                matrix [row].append (rowe)

    # Devuelve la matriz.
    return matrix

# Función checkIfSquared
# Comprueba si el parámetro introducido es una matriz regular sin incógnitas y, si lo es, si es cuadrada o no.
# Además, convierta las matrices introducidas en listas de números en vez de listas de strings.
def checkIfSquared (matrix):
    # Se inicializa un nuevo array que servirá como la matriz una vez convertidos los elementos a números flotantes,
    # ya que al sacarlos de un archivo estos son cadenas de carácteres y no números.
    newMatrix = []

    # La primera dimensión de la matriz, es decir, el número de filas de la matriz.
    # Se obtiene observando el número de listas dentro de la lista que representa la matriz.
    dimension1 = len (matrix)

    # Primero, presuponemos que la matriz es cuadrada.
    squared = 0

    # La segunda dimensión de la matriz, es decir, el número de columnas de esta.
    # Esto equivale a medir el número de elementos por fila,
    # de ahí el nombre de la variable rowe que se verá más adelante durante el programa en reiteradas ocasiones:
    # rowe = Row Element = Elemento de fila.
    dimension2 = len (matrix [0])

    # Por cada fila:
    for row in range (dimension1):
        # Se añade una fila nueva a la nueva matriz.
        newMatrix.append ([])

        # Si la fila no tiene el mismo número de elementos que la primera fila (la segunda dimensión):
        if (len (matrix [row]) != dimension2):
            # Se mantiene la matriz.
            newMatrix = matrix

            # Y se establece que es una matriz de tipo 3 (matriz irregular).
            squared = 3

        # Si la matriz es cuadrada pero tiene elementos que no sean números reales (incógnitas u otras cosas), devuelve 2.
        else:
            for rowe in matrix [row]:
                # Intenta convertir cada elemento a número flotante (y si es un entero tipado como flotante lo convierte a entero) para añadirlo a la nueva matriz.
                try:
                    rowe = floatToInt (float (fracToFloat (rowe)))

                # Si el elemento a analizar no puede convertirse a número flotante:
                except:
                    # Se establece que el parámetro es una matriz de tipo 2 (matriz con incógnitas).
                    squared = 2

                # Independientemente de si ha habido errores a la hora de convertir el elemento en un número:
                finally:
                    # Se añade el elemento a la nueva matriz.
                    newMatrix [row].append (rowe)

    # Si el parámetro introducido es una matriz válida (no es de tipo 2 ni de tipo 3, es decir, ni una matriz irregular ni una matriz con incógnitas):
    if (squared != 2 and squared != 3):
        # Si el número de filas no es igual al número de columnas:
        if (dimension1 != dimension2):
            # La matriz no es cuadrada (tipo 1).
            squared = 1

    # Devuelve el parámetro (con los elementos convertidos a números flotantes si se puede), su tipo y sus dimensiones.
    return newMatrix, squared, dimension1, dimension2

# Función identityMatrix
# Genera una matriz de identidad en función de las dimensiones de la matriz especificada por el usuario.
def identityMatrix (dimension):
    # Primero, se declara la matriz identidad como un array vacío.
    idMatrix = []

    # Si el número de la fila es el mismo que el de la columna, añade un 1. En caso contrario, añade un 0.
    # De este modo se rellena la diagonal principal con 1 y el resto con 0.
    #
    # Se realiza el siguiente proceso fila por fila hasta que el número de filas sea igual al orden de la matriz identidad a generar.
    for row in range (dimension):
        # Se añade una fila sin nada dentro.
        idMatrix.append ([])

        # Se rellena la fila con 1 y 0.
        for rowe in range (dimension):
            # Si el índice del elemento equivale al índice de la fila, añade un 1.
            if (rowe == row):
                idMatrix [row].append (1)

            # Si el índice del elemento es distinto del índice de la fila, añade un 0.
            else:
                idMatrix [row].append (0)

    # Devuelve la matriz identidad de orden n asociada a la matriz cuadrada de orden n que el usuario ha introducido.
    return idMatrix

# Función calculateDeterminant
# Calcula el determinante de la matriz.
def calculateDeterminant (matrix, factor, swapRowsCount):
    # Al determinante le es asignado 1 como valor inicial porque es el elemento neutro del producto.
    determinant = 1

    # Primero realiza una iteración por cada fila de la matriz:
    for row in range (len (matrix)):
        # Luego, realiza una iteración por cada elemento de cada fila:
        for rowe in range (len (matrix [row])):
            # Si el índice del elemento es el mismo que el de la fila (pertenece a la diagonal principal),
            # multiplica el valor actual del determinante por el del elemento.
            if (row == rowe):
                determinant *= matrix [row] [rowe]

    # Multiplica el determinante por el factor, es decir, el producto de los valores por los que se han dividido las filas de la matriz.
    determinant *= factor

    # El número de veces que la operación para intercambiar filas se ha realizado se tiene en cuenta
    # para cambiar el signo del determinante. Cambiar el signo significa multiplicar por (-1)^n,
    # siendo n el número de veces que la operación se ha realizado. Si n es impar, se cambia el signo.
    # Si es par, en cambio, se deja tal y como está.
    if (swapRowsCount % 2 != 0):
        determinant = -determinant

    # Si el determinante es en realidad un número entero tipado como flotante, lo convierte a entero.
    determinant = floatToInt (determinant)

    # Devuelve el determinante de la matriz.
    return determinant

# Función matrixProperties
# Sirve como una especie de "backbone" del modo matricial del programa, ya que actúa como punto de inicio de muchas de las operaciones
# como pueden ser transformar la matriz a una matriz escalonada, calcular el determinante, invertirla,
# comprobar la validez de los parámetros introducidos, declarar la tabla de operaciones y rellenar la lista de propiedades de la matriz.
def matrixProperties (matrix):
    # Se reciben los siguientes parámetros de la función checkIfSquared:
    # - matrix: la matriz con los elementos convertidos a números flotantes.
    # - squared: el código numérico que especifica si el parámetro introducido es una matriz o no y, en caso de que lo sea, si es cuadrada o no.
    # - dimension1: la primera dimensión de la matriz (número de filas).
    # - dimension2: la segunda dimensión de la matriz (número de columnas).
    matrix, squared, dimension1, dimension2 = checkIfSquared (matrix)

    # Se crean dos copias de la matriz para poder transformarlas sin cambiar la matriz original.
    # Sé que no es la forma más óptima de hacerlo, pero no sé muy bien cuál es la lógica de Python a la hora de asignar variables
    # ya que hay cosas que parecen completamente lógicas que, sin embargo, fallan.

    # La primera sirve para calcular el rango.
    matrixForRank = matrix [:]

    # Inicializa la lista de propiedades de la matriz con los dos primeros elementos: el propio parámetro y su tipo.
    properties = [matrix, squared]

    # Si el argumento es una matriz regular (no importa si es cuadrada o no), añade los siguientes elementos a la lista de propiedades:
    if (squared == 0 or squared == 1):
        # El número de filas.
        properties.append (dimension1)

        # El número de columnas.
        properties.append (dimension2)

        # El rango de la matriz.
        properties.append (matrixRank (matrixForRank))

        # La matriz transpuesta.
        properties.append (transposeMatrix (matrix, dimension1, dimension2))

        # Si la matriz es cuadrada, calcula el determinante.
        if (squared == 0):
            # Se inicializa la tabla de operaciones como un array vacío.
            # Las diferentes funciones que se vayan ejecutando irán rellenando esta tabla,
            # que contendrá las operaciones que deben realizarse para obtener la matriz inversa a partir de la matriz identidad si es que la matriz es invertible.
            optable = []

            # Se genera una matriz identidad del mismo orden que la matriz original y se añade a la lista de propiedades de la matriz.
            properties.append (identityMatrix (dimension1))

            # Si el rango de la matriz equivale al número de filas, calcula el determinante.
            # Ya que en caso contrario sería 0.
            if (properties [4] == dimension1):
                # La segunda copia de la matriz sirve para calcular el determinante y la matriz inversa.
                # He decidido crearla ahora para ahorrar recursos en caso de que no hiciese falta calcular el determinante de la matriz
                # debido a que el rango no fuese igual que el número de filas, ya que en ese caso el determinante sería 0.
                matrixToTransform = matrix [:]

                # Devuelve la matriz transformada para calcular el determinante, el factor por el que se multiplica el determinante,
                # el número de veces que se ha realizado la operación de intercambiar filas y el estado actual de la tabla de operaciones.
                # Como argumentos se introducen la matriz, el factor por el que se multiplica el determinante,
                # el número de veces que se han intercambiado las filas y la tabla de operaciones.
                # Como todavía no se le ha hecho nada a la matriz, el factor y el contador de intercambio de filas entran con un valor de 1 y 0.
                matrixToTransform, factor, swapRowsCount, optable = rowEchelonMatrix (matrixToTransform, 1, 0, optable)

                # Calcula el determinante mediante operaciones de filas, es decir, realiza operaciones entre filas hasta conseguir una matriz escalonada.
                # Una vez tiene una matriz escalonada, multiplica los elementos de la diagonal principal
                # (el conjunto de los elementos cuyo índice coincide con el de la fila en la que se encuentran).
                # Ese producto será el determinante.
                determinant = calculateDeterminant (matrixToTransform, factor, swapRowsCount)

                # Se añade el determinante a la lista de propiedades de la matriz.
                properties.append (determinant)

                # Se empieza el proceso de invertir la matriz mediante el algoritmo de Gauss.

                # Primero, se recaba el conjunto de operaciones necesarias para transformar la matriz original en la matriz identitidad.
                # Para ahorrar tiempo y recursos, partimos de la matriz escalonada que se ha usado para calcular el determinante.
                optable = rowEchelonToIdentityMatrix (matrixToTransform, optable) [0]

                # Por último, se inverte la matriz aplicando las operaciones en la tabla de operaciones a la matriz identidad
                # y se añade a la lista de propiedades de la matriz.
                properties.append (invertMatrix (identityMatrix (dimension1), optable))

                # Se añade la tabla de operaciones a la lista de propiedades de la matriz.
                properties.append (optable)

            # Si el rango es diferente al número de filas:
            else:
                # El determinante es 0, por lo tanto se añade a la lista de propiedades.
                # Como el determinante es 0, se determina que la matriz no es invertible así que no hace falta realizar ningún tipo de proceso extra.
                properties.append (0)

    # Devuelve la lista de propiedades de la matriz.
    return properties

# Función rowEchelonMatrix
# Transforma la matriz las veces que haga falta hasta llegar a tener una matriz escalonada.
# También se mantiene un registro de las operaciones que se han realizado.
def rowEchelonMatrix (matrix, factor, swapRowsCount, optable):
    # Se reordenan las filas de la matriz para que aquellas filas que tengan más elementos nulos a la izquierda del pivote
    # tengan un índice mayor que aquellas con un número de ceros a la izquierda del pivote más reducido. Por ejemplo,
    # 0 1 2 3    1 2 3 4
    #    ⇅    ⭢
    # 1 2 3 4    0 1 2 3
    # Se añade lo que se ha hecho a la tabla de operaciones.
    matrix, swapRowsCountRise, optable = orderRows (matrix, optable)

    # Se incrementa el contador de veces que se ha realizado la operación de intercambio de filas
    # en el número de veces que haya tenido que realizarse para ordenar la matriz.
    swapRowsCount += swapRowsCountRise

    # Una vez ordenadas las filas de la matriz, se convierte el pivote de la primera fila en 1.
    # Se vuelve a actualizar la tabla de operaciones.
    matrix, pivot, optable = divideByPivot (matrix, 0, optable)

    # Y se multiplica el factor antes mencionado por el inverso del número por el que se ha dividido la fila, es decir,
    # por el pivote de la fila antes de que la multiplicación lo dejase en 1.
    factor *= pivot

    # Resta (o suma) filas para crear columnas de ceros debajo de los elementos que tengan el mismo índice de fila y de columna.
    # Como cada fila tiene que tener un número de ceros a la izquierda del pivote igual que su índice,
    # realiza la operación a cada fila con aquellas que tengan un índice inferior.
    # Por ejemplo, para hacer que el pivote de la fila 3 sea el tercer elemento, primero se le resta a la fila 3 la fila 1
    # y luego se realiza la misma operación pero con la fila 2.
    for row1 in range (len (matrix)):
        # Debido a la explicación anterior, la fila 2 de la operación irá en función de la fila 1.
        for row2 in range (row1):
            # Debido a problemas con los índices de los pivotes al calcularlos usando la función countZerosRow (), si la fila no es nula:
            if (not nullRow (matrix [row2])):
                matrix, optable = rowEchelonRow (matrix, row1, row2, optable)

    # Se comprueba si tras realizar las operaciones la matriz se ha transformado en una matriz escalonada.
    # Si no es así, se realiza el proceso de nuevo.
    if (not checkIfRowEchelon (matrix)):
        matrix, factor, swapRowsCount, optable = rowEchelonMatrix (matrix, factor, swapRowsCount, optable)

    # Devuelve la matriz escalonada, el factor por el que hay que multiplicar el determinante, el contador de veces que se ha realizado la operación
    # de intercambio de filas y la tabla de operaciones.
    return matrix, factor, swapRowsCount, optable

# Función matrixRank
# Determina el rango de la matriz introducida, que es el número de filas linealmente independientes
# (aquellas que no pueden ser representadas como una combinación lineal de otras filas).
def matrixRank (matrix):
    # Se genera una matriz escalonada a partir de la matriz original.
    # Se hace esto porque el rango de la matriz escalonada escalonada (llamémosla X) es el mismo
    # que el de la matriz original (llamémosla A), en otras palabras, rg(A) = rg(X)

    # Pese a que la función de generar matrices escalonadas tenga 4 salidas, solo nos interesa la primera
    # (aquella con índice 0) y ya que el cálculo del rango de la matriz es un proceso independiente
    # no necesitamos que las entradas que no sean la propia matriz tengan un valor relevante.
    equivalentMatrix = rowEchelonMatrix (matrix, 1, 0, []) [0]

    # Establece el contador de filas nulas a 0, ya que en un principio asumimos que todas las filas son no nulas.
    nNullRows = 0

    # Por cada fila:
    for row in equivalentMatrix:
        # Si la fila es nula se incrementa el contador de filas nulas en 1.
        if (nullRow (row)):
            nNullRows += 1

    # El rango de la matriz equivale al número de filas menos el número de filas nulas de la matriz equivalente.
    rank = len (equivalentMatrix) - nNullRows

    # Devuelve el rango de la matriz
    return rank

# Función nullRow
# Comprueba si la fila es nula, es decir, si todos los elementos de la fila son ceros.
def nullRow (row):
    # Se establece una variable que funciona como un indicador de nulidad de la fila.
    # En un principio asumimos que todos los elementos de la fila son nulos.
    nullRow = True

    # Se comprueba cada elemento de la fila:
    for rowe in row:
        # Si se llega a un elemento no nulo (!= 0), se establece la fila como no nula y se para el proceso.
        if (rowe != 0):
            nullRow = False
            break

    # Devuelve el indicador de nulidad de la fila.
    return nullRow

# Función rowEchelonToIdentityMatrix
# Esta función convierte la matriz escalonada (triangular superior) que se ha generado anteriormente para calcular el determinante
# en una matriz que además de ser triangular superior es triangular inferior, es decir, diagonal.
# Luego, divide las filas entre su pivote para que la matriz se convierta en la matriz identidad.
# Al igual que la función de transformar la matriz, esta función guarda un registro de las operaciones que se han realizado
# con el fin de poder aplicárselas a la matriz identidad.
#
# Esta función también sirve para resolver sistemas de ecuaciones por el algoritmo de Gauss-Jordan, ya que las matrices creadas con esta función
# serán matrices aumentadas en las que todas las columnas menos la última formarán una matriz de coeficientes equivalente a una matriz identidad
# de orden n mientras la última columna contiene los valores de las incógnitas, que son los pivotes de las filas de la matriz antes mencionada.
def rowEchelonToIdentityMatrix (matrix, optable):
    # Divide cada fila por su pivote y actualiza el registro de operaciones.
    for row in range (len (matrix)):
        matrix, pivot, optable = divideByPivot (matrix, row, optable)

    # Se declara una constante de iteración (i).
    for i in range (len (matrix)):
        # La fila 2 (la fila que servirá para transformar a la fila 1) es la fila cuyo índice equivale
        # al de la constante de iteración empezando por atrás, es decir, el número de filas de la matriz menos i.
        row2 = len (matrix) - 1 - i

        # La fila 1 siempre será anterior a la fila 2, por lo que va en función de su rango.
        for row1 in range (row2):
            # Se determina el factor por el que se va a multiplicar la segunda fila a la hora de restársela a la primera.
            factor = matrix [row1] [row2] / matrix [row2] [row2]

            # Siempre que el índice empezando por atrás de la fila con la que se va a operar
            # sea mayor que el de la fila a la que se realizará la operación y el factor no sea 0
            # (porque sumar o restar algo multiplicado por 0 es lo mismo que no hacer nada):
            if (row2 > row1 and factor != 0):
                # Se realiza la operación.
                matrix [row1] = substractRows (matrix [row1], matrix [row2], factor)

                # Y se actualiza el registro de operaciones.
                optable.append ([2, row1, row2, factor])

    # Devuelve la tabla de operaciones.
    # También devuelve la matriz, que es útil para resolver sistemas de ecuaciones pero da igual a la hora de invertir las matrices
    # ya que va a ser usada la matriz identidad generada con la función identityMatrix.
    return optable, matrix

# Función invertMatrix
# Se inverte la matriz aplicándole las operaciones en la tabla de operaciones a la matriz identidad.
def invertMatrix (matrix, optable):
    # Por cada operación en la tabla de operaciones:
    for operation in optable:
        # Comprueba el código de operación, es decir, el primer elemento de la lista.

        # Si es 0, la operación es multiplicar una fila por una constante.
        # Esta operación consta de dos argumentos:
        # - La fila a multiplicar.
        # - El factor por el que se multiplica (o divide) la fila.
        if (operation [0] == 0):
            matrix [operation [1]] = multiplyRow (matrix [operation [1]], operation [2])

        # Si es 1, la operación es intercambiar filas.
        # Esta operación consta de dos argumentos:
        # - Fila 1.
        # - Fila 2.
        elif (operation [0] == 1):
            matrix = swapRows (matrix, operation [1], operation [2])

        # Si es 2, la operación es restar filas.
        # Esta operación consta de tres argumentos:
        # - Fila 1: la fila a transformar.
        # - Fila 2: la fila que opera con la fila 1.
        # - Factor: el valor por el que se multiplican los elementos de la fila 2 antes de restarsélos a sus análogos de la fila 1.
        #           Su signo también define si la operación es una resta (signo positivo) o una suma (signo negativo).
        elif (operation [0] == 2):
            matrix [operation [1]] = substractRows (matrix [operation [1]], matrix [operation [2]], operation [3])

    # Devuelve la matriz inversa.
    return matrix

# Función countZerosRow
# Se cuentan los ceros que hay a la izquierda del pivote de la fila (el primer elemento no nulo).
def countZerosRow (row):
    # Se crea un contador de ceros.
    # Se presume por defecto que el número de ceros a la izquierda del pivote es 0.
    nZeros = 0

    # Se declara una variable que actúa como indicador de si el proceso debe seguir o no.
    shouldContinue = True

    # Se comprueba cada elemento en la fila.
    for rowe in range (len (row)):
        # Si el índice del elemento es menor o igual que el de la fila y el elemento es 0, se aumenta el contador de ceros en 1.
        if (row [rowe] == 0):
            # Se incrementa el contador de ceros.
            nZeros += 1

        # Si se llega a un elemento que no valga 0:
        elif (row [rowe] != 0):
            # Se indica que el proceso no debe seguir.
            shouldContinue = False

        # Si se ha indicado que el proceso no debe seguir:
        if (not shouldContinue):
            # Se para.
            break

    # Devuelve el número de ceros a la izquierda del pivote.
    return nZeros

# Función substractRows
# Operación de restar filas que también sirve para sumar filas.
# Filas con las que operar:
# - Fila 1: la fila que se va a cambiar.
# - Fila 2: la fila que multiplicada por un factor se le va a restar a la fila 1.
# - Fila 1': la fila 1 después de la operación.
def substractRows (row1, row2, factor):
    # La fila 1', que es el resultado de la resta (o suma) entre la fila 1 y la fila 2, se declara como vacía al principio.
    # Luego, se le añadirán los elementos pertinentes.
    newRow = []

    # Se realiza la resta entre cada elemento de la fila 1 y aquel de la fila 2 cuyo índice sea el mismo, multiplicando este último por el factor.
    # El resultado se añade a la fila 1'.
    for rowe in range (len (row1)):
            newRow.append (row1 [rowe] - (factor * row2 [rowe]))

    # Debido a cómo Python trata los números flotantes, algunos números que deberían ser 0 acaban siendo números ligeramente superiores a 0
    # al realizar las operaciones de suma y resta. Esto no parece un problema en un principio,
    # pero a la hora de realizar otras operaciones marca una gran diferencia: por ejemplo, a la hora de dividir por el pivote de la fila.
    # He aquí un ejemplo: si una fila debería ser 0 0 0 17 pero se ha generado la fila 0 0 1e-16 17, ahora no se dividirá entre 17 para dejar el pivote en 1,
    # se dividirá entre 1e-16, lo que genera un número exageradamente grande que no tiene nada que ver con el resultado.
    # Por ello:

    # Cambiando el valor de esta variable se puede ajustar la sensibilidad del programa a la hora de cambiar números muy pequeños a 0.
    numberToZero = 1e-9

    # Se analiza cada elemento de la nueva fila:
    for rowe in range (len (newRow)):
        # Si el elemento varía muy ligeramente respecto a 0:
        if (newRow [rowe] >= -numberToZero and newRow [rowe] <= numberToZero):
            # Se sustituye el elemento por 0.
            newRow [rowe] = 0

    # Devuelve la fila resultante de restar o sumar la fila 2 a la fila 1
    return newRow

# Función checkIfRowEchelon
# Comprobar si la matriz es escalonada/triangular superior.
# En caso contrario, vuelve a transformar la matriz.
def checkIfRowEchelon (matrix):
    # Primero, se presupone que la matriz aún no es una matriz escalonada.
    rowechelon = False

    # Si la matriz solo tiene un elemento siempre es escalonada.
    if (len (matrix) == 1):
        rowechelon = True
    
    else:
        # Comprueba fila por fila si el número de elementos nulos antes del pivote corresponde al índice de la fila (empezando por el 0).
        for row in range (len (matrix)):
            # Comprueba elemento por elemento:
            for rowe in range (len (matrix [row])):
                # Si la fila no es la primera (la fila con índice 0).
                if (row != 0):
                    # Si el elemento en caso de no ser nulo tiene un índice inferior al de la fila.
                    if (rowe < row):
                        # Si el elemento no es nulo.
                        if (matrix [row] [rowe] != 0):
                            # La matriz no es escalonada.
                            rowechelon = False

                    # Si no se cumple la primera condición, es que la matriz de momento es escalonada.
                    else:
                        rowechelon = True

    # Devuelve un booleano (True o False) que indica si la matriz es escalonada o no.
    return rowechelon

# Función orderRows
# Ordena las filas de la matriz en función del número de ceros que tengan a la izquierda del pivote.
def orderRows (matrix, optable):
    # Primero, dejamos el contador de veces que se realiza la operación de intercambio de filas en 0, pues todavía no ha sido realizada ni una sola vez.
    swapRowsCount = 0

    # Comparamos las filas:
    # La fila 1 es la fila que toque en ese momento siguiendo una iteración desde la primera fila a la última.
    for row1 in range (len (matrix)):
        # La fila 2 sigue el mismo criterio que la fila 1.
        for row2 in range (len (matrix)):
            # Siempre y cuando el índice de la fila 2 sea menor que el de la 1:
            if (row1 > row2):
                # Si la fila 1 de la comparación tiene más ceros a la izquierda del pivote que la fila 2
                if (countZerosRow (matrix [row1]) > countZerosRow (matrix [row2])):
                    # Se realiza la operación de intercambio de filas entre la fila 1 y la fila 2.
                    matrix = swapRows (matrix, row1, row2)

                    # Se incrementa en 1 el contador de veces que se realiza la operación de intercambio de filas.
                    swapRowsCount += 1

                    # Se actualiza la tabla de operaciones.
                    optable.append ([1, row1, row2])

    # Ahora, toca cambiar la primera fila por aquella fila que tenga el primer elemento más grande.

    # Se mira cuál es el índice de la fila con el primer elemento más grande.
    biggestrow = biggestRow (matrix)

    # Si la fila con el primer elemento más grande no es la primera:
    if (biggestrow != 0):
        # Se intercambia la primera fila con esa fila.
        matrix = swapRows (matrix, 0, biggestrow)

        # Se incrementa en 1 el contador de veces que se realiza la operación de intercambio de filas.
        swapRowsCount += 1

        # Se actualiza el registro de operaciones.
        optable.append ([1, 0, biggestrow])

    # Devuelve la matriz con las filas cambiadas, la cantidad de veces que se ha realizado la operación de cambiar filas y la tabla de operaciones.
    return matrix, swapRowsCount, optable

# Función divideByPivot
# Divide la fila fila por su pivote, es decir, su primer elemento no nulo.
# De este modo, el pivote será 1 ya que n/n = 1.
# Como consecuencia, el resto de elementos de la fila también se dividirán por el pivote.
# Además, el determinante será multiplicado por el pivote de la fila con la que se operará.
# También, se registra la operación en la tabla de operaciones.
def divideByPivot (matrix, row, optable):
    # Se almacena el valor del pivote para que no se pierda al sustituir la fila antes de la operación por la fila después de la operación.
    pivot = matrix [row] [countZerosRow (matrix [row])]

    # Comprueba que el pivote de la primera fila no sea 0 y tampoco 1, si no lo es,
    # divide toda la fila por el pivote para que este se convierta en 1.
    # Esto es debido a que dividir 1 entre 1 da lo mismo porque 1 es el elemento neutro de la división
    # (por lo que evitamos registar una operación inútil en la tabla)
    # y dividir entre 0 hace que el valor no se encuentre en el conjunto de los números reales. Además, 0/0 no está definido.
    if (pivot != 0 and pivot != 1):
        newRow = multiplyRow (matrix [row], pivot)

        # De nuevo, se actualiza el registro de operaciones.
        optable.append ([0, row, pivot])

        # Sustituye la fila original por la fila dividida por su pivote.
        matrix [row] = newRow

    # Devuelve la nueva matriz en la que la fila a manipular ha sido dividida por su pivote, el pivote y la tabla de operaciones.
    return matrix, pivot, optable

# Función multipyRow
# Operación de multiplicar una fila por una constante.
def multiplyRow (row, factor):
    # La fila transformada empieza siendo declarada como una lista vacía.
    newRow = []

    # Se multiplica cada elemento de la fila por la constante.
    for rowe in row:
        newRow.append (rowe / factor)

    # Devuelve la fila transformada.
    return newRow

# Función swapRows
# Operación de intercambio de filas.
# La fila 1 ahora equivale a la fila 2 antes del cambio y la fila 2 ahora equivale a la fila 1 antes del cambio.
def swapRows (matrix, row1, row2):
    # Declara una fila 2' que equivale a la fila 1.
    newRow1 = matrix [row2]

    # Declara una fila 1' que equivale a la fila 2.
    newRow2 = matrix [row1]

    # Sustituye la fila 1 por la fila 1'.
    matrix [row1] = newRow1

    # Sustituye la fila 2 por la fila 2'.
    matrix [row2] = newRow2

    # Devuelve la matriz con las filas 1 y 2 intercambiadas.
    return matrix

# Función rowEchelonRow
# Se transforma la fila en una fila que haga que la matriz puede satisfacer
# los requisitos necesarios para ser una matriz escalonada.
def rowEchelonRow (matrix, row1, row2, optable):
    # Se compara el pivote de la fila 2 con aquel de la primera fila que posee su mismo índice.
    # El número que resulta de su multiplicación es el factor que servirá para multiplicar los elementos de la fila 2 a la hora de restar.
    # Además, si el factor es negativo se realizará una suma.

    # El índice del pivote de la segunda fila equivale al número de ceros de la fila.
    pivot = countZerosRow (matrix [row2])

    # Si el pivote de la segunda fila es distinto de 0, el factor será la cifra que cumpla el criterio anteriormente mencionado
    # y se realizará la operación de resta o suma de filas.
    # Si es 0, en cambio, no se necesitará hacer nada.
    if (matrix [row2] [pivot] != 0):
        factor = matrix [row1] [pivot] / matrix [row2] [pivot]

        # Se realiza la operación de restar filas.
        newRow = substractRows (matrix [row1], matrix [row2], factor)

        # Como 0 es el elemento neutro de la suma y de la resta, siempre y cuando el factor no sea 0.
        if (factor != 0):
            # Se actualiza el registro de operaciones.
            optable.append ([2, row1, row2, factor])

        # En la matriz, se sustituye la fila 1 por la fila 1'.
        matrix [row1] = newRow

    # Devuelve nueva matriz en la que la fila 1 ha sido sustituida por la fila 1'.
    # Si no se ha hecho nada, la nueva matriz es la misma que la original.
    # También devuelve el registro de operaciones actualizado.
    return matrix, optable

# Comparar las filas para ver cuál tiene más "grande" (valor absoluto mayor) el primer elemento.
# Filas a comparar:
# - Fila 1: Candidata a fila más grande.
# - Fila 2: Fila más grande actual.
def biggestRow (matrix):
    # Primero, asumimos que la fila más grande es la primera (aquella con índice 0).
    biggestrow = 0

    # Luego, vemos si hay una fila más grande. Si la hay, esa ocupará el puesto de fila más grande.
    # Así sucesivamente hasta que se acaben las filas por analizar.
    for row in range (len (matrix)):
        # Se comparan los primeros elementos de la fila considerada como más grande y la fila a analizar.
        # Si la fila a analizar tiene el primer elemento más grande:
        if (abs (matrix [row] [0]) > abs (matrix [biggestrow] [0])):
            # Ocupa su lugar como la fila más grande.
            biggestrow = row

    # Devuelve el índice de la fila más grande.
    return biggestrow

# Función transposeMatrix
# Genera la matriz transpuesta de la matriz de entrada.
# Una matriz transpuesta es una matriz en la que los elementos que previamente se encontraban en las columnas ahora se encuentran en las filas y viceversa.
# Podría decirse que generar una matriz transpuesta consiste en reflejar los elementos de una matriz sobre su diagonal, así los índices de los elementos cambian.
# Por ejemplo, si un elemento tiene el índice (1, 3) en la matriz original, en la matriz transpuesta tendría el índice (3, 1).
def transposeMatrix (matrix, dimension1, dimension2):
    # Se declara la matriz transpuesta como una lista vacía, que pasará a ser un array bidimensional.
    tMatrix = []

    # Por cada columna en la matriz original se añade una fila en la matriz transpuesta.
    for rowe in range (dimension2):
        tMatrix.append ([])
        # Por cada fila en la matriz original se añade un 0 (para rellenar) a cada una de las filas de la matriz transpuesta.
        for row in range (dimension1):
            tMatrix [rowe].append (0)

    # Se iteran las filas de la matriz transpuesta:
    for row in range (len (matrix)):
        # Por cada fila se iteran los elementos, es decir, las columnas:
        for rowe in range (len (matrix [row])):
            # Se sustituyen los ceros de la matriz transpuesta por los elementos de la matriz original
            # cuyo índice sea el índice de la columna y el índice de la fila, en ese orden.
            tMatrix [rowe] [row] = matrix [row] [rowe]

    # Devuelve la matriz transpuesta.
    return tMatrix

# Función createOutputFile
# Crea el archivo de salida al que se exportarán los sistemas de ecuaciones lineales y las matrices,
# pero antes comprueba si ya hay un archivo con el mismo nombre. En tal caso, le cambia el nombre a la versión anterior para que siga guardada.
def createOutputFile (path):
    # Si el archivo de salida ya existe:
    if (os.path.exists (path)):
        # El nombre de la copia de seguridad será "<archivo>.output.pre-<Año>-<Mes>-<Día>_<Hora>_<Minuto>_<Segundo>".
        backupFile = path + '.pre-' + executionDate

        # Si ya existe una copia de seguridad del archivo (porque se ha ejecutado el programa varias veces en el mismo segundo):
        if (os.path.exists (backupFile)):
            # Se borra.
            os.remove (backupFile)

        # Se le cambia el nombre al archivo para no borrarlo.
        os.rename (path, backupFile)

    # Se crea el archivo de salida.
    outputFile = open (path, 'x')

    # Se cierra el archivo de salida.
    outputFile.close ()

# Función exportMatrixList
# Se exportan cada matriz de la lista y sus propiedades al archivo de salida que corresponda según la configuración.
def exportMatrixList (propertyList):
    # Se establece la ruta del archivo de salida como la ruta del archivo especificado en la opción 'path' más la extensión '.output'.
    path = config ['path'] + '.output'

    # Crea el archivo de salida.
    createOutputFile (path)

    # Abre el archivo de salida para escribir las matrices y sus propiedades en él.
    # Lo abre como un archivo codificado en unicode para escribir carácteres como '┌' o '┐'.
    outputFile = open (path, 'a', encoding = 'utf-8')

    # Se escriben todos los conjuntos de propiedades de matriz en el archivo.
    # Por cada conjunto:
    for properties in range (len (propertyList)):
        # Si no es la primera matriz:
        if (properties != 0):
            # Añade dos líneas en blanco.
            outputFile.write ('\n\n\n')

        # Se escribe un título para la matriz, pero convirtíendo el número de la matriz de índice 0 a índice 1.
        outputFile.write ('Matriz ' + str (properties + 1) + ':')

        # Se escribe la matriz original en el formato elegido en la opción 'style' (con todos los elementos que se puedan convertidos a enteros).
        outputFile.write ('\n\n  Matriz:' + matrixToString (propertyList [properties] [0], config ['style']))

        # Si el parámetro es una matriz (da igual si es cuadrada o no):
        if (propertyList [properties] [1] == 0 or propertyList [properties] [1] == 1):
            # Si la opción 'dimensions' está activada:
            if (config ['dimensions'] == 1):
                # Se escribe el número de filas:
                outputFile.write ('\n\n  Número de filas: ' + str (propertyList [properties] [2]))

                # Se escribe el número de columnas:
                outputFile.write ('\n\n  Número de columnas: ' + str (propertyList [properties] [3]))

            # Si la opción 'rank' está activada:
            if (config ['rank'] == 1):
                # Se escribe el rango de la matriz:
                outputFile.write ('\n\n  Rango: ' + str (propertyList [properties] [4]))

            # Si la opción 'transpose' está activada:
            if (config ['transpose'] == 1):
                # Se escribe la matriz transpuesta:
                outputFile.write ('\n\n  Matriz transpuesta:' + matrixToString (prettifyMatrixElements (propertyList [properties] [5]), str (config ['style'])))

            # Si la matriz es cuadrada:
            if (propertyList [properties] [1] == 0):
                # Si la opción 'idmatrix' está activada:
                if (config ['idmatrix'] == 1):
                    # Se escribe la matriz identidad.
                    outputFile.write ('\n\n  Matriz identidad:' + matrixToString (prettifyMatrixElements (propertyList [properties] [6]), str (config ['style'])))

                # Si la opción 'determinant' está activada:
                if (config ['determinant'] == 1):
                    # Se escribe el determinante de la matriz.
                    outputFile.write ('\n\n  Determinante: ' + str (propertyList [properties] [7]))

                # Si la matriz es invertible, es decir, si el número de elementos en su lista de propiedades equivale a 9:
                if (len (propertyList [properties]) == 10):
                    # Se escribe la matriz inversa.
                    # Esta es una parte obligatoria del programa, ya que pese a tener unas cuantas funciones más quiero que mantenga su espíritu original:
                    # ser un inversor de matrices.
                    outputFile.write ('\n\n  Matriz inversa:' + matrixToString (prettifyMatrixElements (propertyList [properties] [8]), config ['style']))

                    # Si la opción 'oplist' está activada, se muestra la lista de operaciones a realizar
                    # para convertir la matriz identidad en la matriz inversa:
                    if (config ['oplist'] == 1):
                        outputFile.write ('\n\n  Operaciones a realizar para invertir la matriz:\n' + parseOperationList (prettifyMatrixElements (propertyList [properties] [9])))

                # En cambio, si la matriz no es invertible.
                else:
                    # Se genera un mensaje de error que avisa de que la matriz no es invertible.
                    outputFile.write ('\n\n  Matriz no invertible')

        # Si el parámetro es una matriz con incógnitas:
        elif (propertyList [properties] [1] == 2):
            # Se describe el problema del parámetro.
            outputFile.write ('\n\n  Parámetro no válido: matriz con incógnitas.')

        # Si el parámetro es una matriz irregular:
        elif (propertyList [properties] [1] == 3):
            # Se describe el problema del parámetro.
            outputFile.write ('\n\n  Parámetro no válido: matriz irregular.')

    # Cierra el archivo de salida.
    outputFile.close ()

# Función parseOperationList
# Función que sirve para hacer que la tabla de operaciones sea transcrita a unas instrucciones que contienen el total de operaciones elementales de filas
# a realizar a la matriz identidad asociada a la matriz cuadrada correspondiente para generar la matriz inversa con el algoritmo de Gauss.
def parseOperationList (optable):
    # Se inicializa el string que contiene las operaciones convertidas en "pasos"
    # (paso = manera legible de interpretar la operación como si fuese parte de un conjunto de instrucciones ordenadas).
    operationListStr = ''

    # Si la tabla de operaciones está vacía, es que no hace falta hacer nada para invertir la matriz.
    if (optable == []):
        # Se incluye el hecho de que no haga falta hacer nada en las instrucciones de inversión.
        operationListStr = '    No hace falta hacer nada para invertir la matriz.'

    # Si la tabla de operaciones no está vacía:
    else:
        # Por cada operación de la lista de operaciones:
        for operation in range (len (optable)):
            # Se inicia el string de la operación con un tabulado de dos espacios (como en el resto de propiedades de la matriz),
            # su índice de paso y un espacio para introducir la operación.
            operationStr = '    ' + str (operation + 1) + '.' + ' '

            # Se escribe la operación en forma de oración según su tipo:

            # Si la operación es de multiplicación (o división) por una constante (código de operación 0):
            if (optable [operation] [0] == 0):
                operationStr += 'Dividir la fila ' + str (optable [operation] [1] + 1) + ' por ' + str (optable [operation] [2]) + '.'

            # Si la operación es de intercambio de filas (código de operación 1):
            elif (optable [operation] [0] == 1):
                operationStr += 'Intercambiar la fila ' + str (optable [operation] [1] + 1) + ' por la fila ' + str (optable [operation] [2] + 1) + '.'

            # Si la operación es de resta (o suma) de filas (código de operación 1):
            else:
                # Si el factor de la operación es un número positivo, la operación es de resta:
                if (optable [operation] [3] > 0):
                    operationStr += 'Restar'

                # En caso contrario, es de suma:
                else:
                    operationStr += 'Sumar'

                # Se escribe la siguiente parte invariable de la instrucción.
                operationStr += ' la fila ' + str (optable [operation] [2] + 1)

                # Si el valor absoluto del factor es 1, no se escribe por qué valor se multiplica la fila 2 para operar con la fila 1,
                # ya que 1 es el elemento neutro de la multiplicación.
                # En caso contrario, se escribe el valor absoluto del factor.
                if (abs (optable [operation] [3]) != 1):
                    operationStr += ' multiplicada por ' + str (abs (optable [operation] [3]))

                # Se escribe la última parte invariable de la instrucción.
                operationStr += ' a la fila ' + str (optable [operation] [1] + 1) + '.'

            # Si la operación no es la última de la lista:
            if (operation < len (optable) - 1):
                # Añade una nueva línea.
                operationStr += '\n'

            # Se añade el string de la operación al conjunto de las operaciones convertido a string.
            operationListStr += operationStr

    # Devuelve la lista de operaciones formateada como una lista ordenada de instrucciones.
    return operationListStr

# Función parseEquationSystemList
# Si el archivo de entrada existe, genera una lista con los sistemas de ecuaciones lineales del archivo de entrada especificado en la función path.
# Esta función es el análogo del modo ecuacional de la función parseMatrixList.
def parseEquationSystemList (path):
    # Abre el archivo de entrada en el que se encuentran los sistemas de ecuaciones a resolver.
    # Se abre como un archivo codificado en UTF-8 para poder leer carácteres como α, β y ω.
    inputFile = open (path, 'r', encoding = 'utf-8')

    # Se inicializa la lista de sistemas de ecuaciones como una lista vacía.
    # Esta lista será un array tetradimensional en el que las dimensiones serán lo siguiente:
    # - Primera dimensión: pares en los que se encuentran la lista de parámetros de cada sistema de ecuaciones
    #                      y los sistemas de ecuaciones representados como matrices.
    # - Segunda dimensión: las matrices anteriormente mencionadas.
    #                      Las matrices están transpuestas, es decir, las filas van en el siguiente orden:
    #                      Fila 1: coeficientes del parámetro 1; fila 2: coeficientes del parámetro 2; ...;
    #                      fila n - 1: coeficientes del parámetro n; fila n: constantes.
    # - Tercera dimensión: las filas de las matrices.
    # - Cuarta dimensión: los elementos de las filas.
    eqSysList = []

    # Se declara un array bidimensional que funcionará como un almacén de sistemas de ecuaciones lineales en bruto.
    # La primera dimensión la conformarán los propios sistemas de ecuaciones y la segunda dimensión serán las propias ecuaciones lineales en forma de string.
    eqSysRawList = [[]]

    # Se declara una variable que funcionará como un contador de sistemas de ecuaciones.
    eqSysIndex = 0

    # Se analiza cada línea del archivo de entrada:
    for line in inputFile:
        # Si la línea está vacía:
        if (line in ['\n', '\r\n']):
            # Significa que hay que pasar a analizar otro sistema de ecuaciones.

            # Se añade un elemento nuevo a la lista de sistemas de ecuaciones en bruto.
            eqSysRawList.append ([])

            # Se incrementa en 1 el contador de sistemas de ecuaciones.
            eqSysIndex += 1

        # Si la línea no está vacía:
        else:
            # Se añade la línea, que es una ecuación, al sistema de ecuaciones que le corresponda según el contador de sistemas de ecuaciones.
            eqSysRawList [eqSysIndex].append (line)

    # Cierra el archivo de entrada.
    inputFile.close ()

    # Se filtran aquellos sistemas de ecuaciones lineales que estén vacíos y se eliminan de la lista.
    # Esto se hace para permitir al usuario separar los sistemas de ecuaciones con el número de líneas que desee entre ellos.
    eqSysRawList = list (filter (None, eqSysRawList))

    # Por cada sistema de ecuaciones en la lista de sistemas en bruto:
    for eqSys in eqSysRawList:
        # Se añade un par compuesto por la lista de parámetros y la matriz transpuesta del sistema.
        eqSysList.append (list (parseEquationSystem (eqSys)))

    # Se filtran aquellos sistemas de ecuaciones que estén vacíos.

    # Se inicializa la lista de soluciones de los sistemas de ecuaciones.
    solutionList = []

    # Por cada sistema de ecuaciones:
    for eqSys in range (len (eqSysList)):
        # Se añade una nueva entrada vacía a la lista.
        solutionList.append ([])

    # Devuelve la lista de sistemas de ecuaciones lineales y la lista de soluciones (de momento vacía) de los sistemas de ecuaciones.
    return eqSysList, solutionList

# Función parseEquationSystem
# Esta función analiza cada sistema de ecuaciones que se le pasa y obtiene la lista de los parámetros de ese sistema de ecuaciones,
# la matriz A y la matriz A' (explicadas más adelante).
def parseEquationSystem (eqSys):
    # Se declara una lista con los operadores.
    # Al ser ecuaciones lineales, los únicos operadores son la suma (+), la resta (-) y la igualdad (=)
    operatorList = ['+', '-', '=']

    # Se inicializa la matriz transpuesta del sistema de ecuaciones.
    matrix = []

    # Se inicializa la lista de incógnitas del sistema de ecuaciones como una lista vacía.
    paramList = []

    # Se inicializa la lista de coeficientes de las variables del sistema de equaciones.
    # Esta lista será un array bidimensional que funcionará como una matriz, la matriz A.
    # Las filas de la matriz A representan la parte izquierda de las ecuaciones del sistema
    # y las columnas son los coeficientes de cada variable.
    # Pasará a tener la estructura mencionada después de transponerla, ya que de momento tendrá la contraria.
    paramCoList = []

    # Se inicializa la lista de soluciones del sistema de ecuaciones.
    # Las soluciones son los valores que no son coeficientes de ninguna variable que están a la derecha del signo igual.
    # Esta lista funciona como una matriz fila que luego se añadirá a la matriz A para formar la matriz A'.
    # Luego, esta matriz se transpondrá.
    constantList = []

    # Se declaran:

    # El indicador de constante (indica si el elemento es una constante o un coeficiente de incógnita)
    isAConstant = False

    # El indicador de negatividad (indica si el elemento es un número negativo o no).
    negativeNumber = False

    # Cada string en la lista del sistema de ecuaciones lineales corresponde a una ecuación.
    # Por cada ecuación:
    for equation in range (len (eqSys)):
        # Se crea una lista con todos los elementos del sistema de ecuaciones, que estarán separados entre ellos mediante espacios.
        elementList = eqSys [equation].split (' ')

        # Si ha habido más de un espacio seguido en la ecuación, se han generado elementos vacíos que se han añadido a la lista de elementos
        # (debido al funcionamiento de la función split (' ')), por lo tanto, tienen que ser eliminados.
        # Para ello, se recorre la lista de términos y se eliminan aquellos que sean strings vacíos.
        for element in elementList:
            if (element == ''):
                elementList.remove (element)

        # Si el elemento contiene el carácter de salto de línea, se lo quita.
        # Esto pasa con el último elemento de cada fila.
        for element in range (len (elementList)):
            if ('\n' in elementList [element]):
                elementList [element] = elementList [element].replace ('\n', '')

        # Se analiza cada elemento de la lista de elementos de la ecuación.
        for element in elementList:
            # Si el elemento pertenece a la lista de operadores:
            if (element in operatorList):
                # Si el elemento es el signo de adición no se hace nada, ya que no se cambia el signo:

                # Si el elemento es el signo de substracción:
                if (element == '-'):
                    # Se invierte el signo del siguiente número (o signo).

                    # Si el indicador de negatividad no está activo:
                    if (not negativeNumber):
                        # Pasa a ser negativo.
                        negativeNumber = True

                    # Si indicador de negatividad está activo:
                    else:
                        # Pasa a ser positivo.
                        negativeNumber = False

                # Si el elemento es el signo igual:
                if (element == '='):
                    # Se establece que el siguiente elemento pertenecerá a la matriz columna
                    # en la que están las soluciones de cada ecuación.
                    isAConstant = True

            # Si el elemento no está en la lista de operadores:
            else:
                # Se simula el mismo bucle do-while que se puede encontrar en la función fracToFloat.
                # Para no ser tan redundante (pese a haberlo sido en muchas ocasiones), no voy a volver a comentar la estructura.
                shouldRestart = True

                while (shouldRestart):
                    shouldRestart = False

                    # Analiza cada carácter del elemento.
                    for char in element:
                        # Si el carácter es el signo positivo:
                        if (char == '+'):
                            # No se invierte el signo del número.

                            # Se quita el carácter del elemento.
                            element = str (element).replace (char, '', 1)

                            shouldRestart = True
                            break

                        # Si el carácter es el signo negativo:
                        elif (char == '-'):
                            # Se invierte el signo del número.

                            # Si el número es positivo:
                            if (not negativeNumber):
                                # Pasa a ser negativo.
                                negativeNumber = True

                            # Si el número es negativo:
                            else:
                                # Pasa a ser positivo.
                                negativeNumber = False

                            # Se quita el carácter del elemento.
                            element = str (element).replace (char, '', 1)

                            shouldRestart = True
                            break

                        # Si el carácter es una coma:
                        if (char == ','):
                            # Se cambia por un punto (por si el usuario quiere introducir los decimales con una coma en vez de un punto).
                            # Se aprovecha para cambiar todas las comas del elemento por puntos.
                            element = str (element).replace (char, '.')

                        # Si el carácter es cualquiera que no sea la barra inclinada (para dividir), el asterico (para multiplicar),
                        # el punto (para los decimales), o los paréntesis (para encapsular cosas):
                        elif (char != '.' and char != '/' and char != '*' and char != '(' and char != ')' and char != '^'):
                            # Si el elemento es una constante:
                            if (isAConstant):
                                # Comprueba si el elemento se puede convertir en un número flotante (y de paso a entero):
                                try:
                                    element = fracToFloat (element)

                                # Si no se puede, significa que el elemento no es una constante:
                                except:
                                    # Se genera un mensaje de error explicando el problema y se sale con el código de error 16.
                                    print ('Las soluciones de las ecuaciones tienen que ser constantes, no pueden ser incógnitas ni parámetros.')
                                    sys.exit (16)

                                # Si el programa sigue en ejecución después de lo anterior, es que se puede convertir el elemento a número flotante.
                                # Eso quiere decir que es una constante.

                                else:
                                    # Si el indicador de negatividad está activado:
                                    if (negativeNumber):
                                        # Se cambia el signo del elemento.
                                        element = -element

                                        # Se reinicia el indicador de negatividad.
                                        negativeNumber = False

                                    # Agrega el elemento a la lista de constantes.
                                    constantList.append (element)

                                    # Se reinicia el indicador de constante.
                                    isAConstant = False

                            # Si el elemento no es una constante:
                            else:
                                # Se comprueba si el carácter en cuestión es un número.
                                try:
                                    float (char)

                                # Si no lo es, es que es una incógnita:
                                except:
                                    # Si no está en la lista de parámetros:
                                    if (char not in paramList):
                                        # Se añade a la lista.
                                        paramList.append (char)

                                        # Se crea una fila nueva en la matriz de los coeficientes de incógnitas.
                                        paramCoList.append ([])

                                    # Quita el parámetro del elemento para poder añadirlo a la lista de coeficientes de los parámetros
                                    # y convierte el elemento a número flotante (o entero si su parte decimal es 0).
                                    element = element.replace (char, '')

                                    # Se obtiene el índice del parámetro en la lista de parámetros.
                                    paramIndex = paramList.index (char)

                                    # Si después de quitar los carácteres que no son números el elemento es un string vacío,
                                    # es que el coeficiente de la incógnita es 1. Por tanto, se sustituye por 1.
                                    if (element == ''):
                                        element = '1'

                                    # Se convierte el elemento de fracción a número flotante (si es que lo es).
                                    # Luego, se convierte el elemento a flotante y, si no cambia su valor, a entero.
                                    element = fracToFloat (element)

                                    # Comprueba si después de todo el elemento es un número:
                                    try:
                                        float (element)

                                    # Si no lo es:
                                    except:
                                        # Se genera un mensaje de error explicando el problema y se sale con el código de error 17.
                                        print ('No se pueden introducir parámetros en los sistemas de ecuaciones.')
                                        sys.exit (17)

                                    # Si el indicador de negatividad está activado:
                                    if (negativeNumber):
                                        # Se cambia el signo del elemento.
                                        element = -element

                                        # Se reinicia el indicador de negatividad.
                                        negativeNumber = False

                                    # Se añade el elemento a la fila de la matriz de coeficientes de incógnitas de la incógnita que le corresponde.

                                    # Se comprueba si ya había un elemento en su fila que fuera coeficiente del mismo parámetro.
                                    try:
                                        paramCoList [paramIndex] [equation]

                                    # Si no lo hay:
                                    except:
                                        # Se añade a su fila de parámetro.
                                        paramCoList [paramIndex].append (element)

                                    # Si lo hay:
                                    else:
                                        # Se suma al elemento previo.
                                        paramCoList [paramIndex] [equation] += element

    # Por cada conjunto de coeficientes de los parámetros del sistema de ecuaciones.
    for paramCoefficients in paramCoList:
        # Se añade como fila a la matriz.
        matrix.append (paramCoefficients)

    # Se añade el conjunto de constantes a la matriz como una fila nueva.
    matrix.append (constantList)

    # Devuelve la lista de parámetros y la matriz transpuesta del sistema de ecuaciones.
    return paramList, matrix

# Función inputEquationSystem
# Esta función permite al usuario introducir un sistema de ecuaciones a través de inputs en vez de a través de un archivo.
# Se usa en la versión Prog en caso de que el usuario desee introducir sistemas de ecuaciones adicionales.
# Es el análogo del modo ecuacional de la función inputMatrix.
def inputEquationSystem ():
    # Se crea una lista vacía que contendrá las ecuaciones.
    eqSys = []

    # Se pide al usuario que introduzca una ecuación lineal hasta que pulse Enter.
    # Para ello, se simula otro bucle do-while.

    shouldRestart = True

    while (shouldRestart):
        # Se limpia la pantalla.
        clearScreen ()

        # Se pregunta al usuario que introduzca una ecuación.
        equation = input ('Introduce una ecuación lineal [Enter para terminar]: ')

        # Si la respuesta del usuario es un string vacío, es decir, ha pulsado Enter sin introducir nada:
        if (equation == ''):
            # Se establece que el bucle no se repetirá.
            shouldRestart = False

        # En caso contrario:
        else:
            # Se añade la ecuación a la lista de ecuaciones.
            eqSys.append (equation)

    # Se transforma la lista de ecuaciones en forma de string a un sistema de ecuaciones en forma de matrices con una lista de sus parámetros.
    eqSys = parseEquationSystem (eqSys)

    # Devuelve el sistema de ecuaciones.
    return eqSys

# Función solveEquationSystem
# Esta función saca la lista de incógnitas de cada sistema de ecuaciones y crea las matrices de coeficientes y aumentadas.
# Analiza el sistema de ecuaciones y determina su tipo. Si es un sistema compatible determinado, resuelve el sistema por el algoritmo de Gauss-Jordan
# y asigna a cada incógnita su valor.
def solveEquationSystem (eqSys):
    # Se saca la lista de parámetros del sistema de ecuaciones.
    paramList = eqSys [0]

    # Se inicializa la matriz de coeficientes como una lista vacía.
    coMatrix = []

    # Se rellena la matriz de coeficientes con todas las filas de la matriz transpuesta del sistema de ecuaciones menos la última,
    # que es la fila de las constantes.
    for coefficientRow in range (len (eqSys [1]) - 1):
        coMatrix.append (eqSys [1] [coefficientRow])

    # Se transpone la matriz de coeficientes tranpuesta. Así, ya tenemos la matriz A lista para operar con ella.
    coMatrix = transposeMatrix (coMatrix, len (coMatrix), len (coMatrix [0]))

    # Se crea la matriz aumentada transpuesta con todas las filas de la matriz transpuesta del sistema de ecuaciones.
    # Luego, se transpone para conseguir la matriz A'.
    augMatrix = transposeMatrix (eqSys [1], len (eqSys [1]), len (eqSys [1] [0]))

    # Al igual que pasa en el modo matricial, hay que crear copias de las matrices para analizar su rango.
    coMatrixForAnalysis = coMatrix [:]
    augMatrixForAnalysis = augMatrix [:]

    # Analiza el sistema de ecuaciones y devuelve un entero indicando su tipo en el intervalo [0, 2] indicando su tipo.
    # Además, devuelve el número de ecuaciones que sobran en caso de que el sistema sea compatible determinado y haya más ecuaciones que incógnitas.
    eqSysType, rankDiff = analyzeEquationSystem (coMatrixForAnalysis, augMatrixForAnalysis, len (paramList))

    # Crea la lista de propiedades del sistema con su tipo como primer elemento.
    systemProperties = [eqSysType]

    # Si el sistema es compatible indeterminado (tipo 1):
    if (eqSysType == 2):
        # Convierte la matriz aumentada en una matriz escalonada aprovechando la función rowEchelonMatrix () del modo matricial.
        # Como no vamos a calcular determinantes ni a invertir ninguna matriz,
        # las 3 últimas entradas no tienen importancia alguna y solo se usará la primera salida.
        augMatrix = rowEchelonMatrix (augMatrix, 1, 0, []) [0]

        # Antes de pasar a la última fase del algoritmo de Gauss-Jordan, se eliminan las ecuaciones que sobran.
        # Estas son aquellas que han quedado anuladas a la hora de escalonar la matriz.

        # Para ello, se iteran las ecuaciones:
        for equation in range (len (augMatrix)):
            # Si la fila que representa la ecuación es nula:
            if (nullRow (augMatrix [equation])):
                # Se elimina de la matriz aumentada.
                augMatrix.pop (equation)

        # Convierte la matriz aumentada escalonada en una matriz escalonada reducida aprovechando la función rowEchelonToIdentityMatrix () del modo matricial.
        # Como no vamos a invertir ninguna matriz, la tabla de operaciones no es relevante y solo se tendrá en cuenta la primera salida.
        augMatrix = rowEchelonToIdentityMatrix (augMatrix, []) [1]

        # Se transpone la matriz escalonada reducida porque asi no hace falta manejar la segunda dimensión del array bidimensional,
        # ya que así se puede añadir la última columna de la matriz original (la de constantes) a la lista de propiedades manejándola como si fuese una fila,
        # es decir, un elemento en la primera dimensión.
        augMatrix = transposeMatrix (augMatrix, len (augMatrix), len (augMatrix [0]))

        # Se añade la lista de incógnitas a la lista de propiedades del sistema.
        systemProperties.append (paramList)

        # Se añade la fila de los valores de las incógnitas a la lista de propiedades del sistema.
        systemProperties.append (augMatrix [len (augMatrix) - 1])

    # Devuelve la lista de propiedades del sistema de ecuaciones, cuya longitud dependerá de su tipo.
    return systemProperties

# Función analyzeEquationSystem ()
# Determina si el sistema de ecuaciones lineales es incompatible, compatible indeterminado o compatible determinado.
# Lo hace analizando el rango de la matriz de coeficientes y de la matriz aumentada y el número de incógnitas.
# También devuelve la diferencia entre el rango y el número de incógnitas si el sistema es compatible determinado, es decir, el número de ecuaciones que sobran.
def analyzeEquationSystem (coMatrix, augMatrix, nParams):
    # Se declara una variable que especifica el tipo de sistema de ecuaciones.
    # Estos son los valores posibles:
    # - 0: Sistema incompatible.
    # - 1: Sistema compatible indeterminado.
    # - 2: Sistema compatible determinado.
    # Se le da el valor de 0 por defecto símplemento por darle un valor.
    eqSysType = 0

    # Se establece que la diferencia entre el rango y el número de incógnitas es 0 por defecto, ya que con 0 como valor la variable no tiene uso alguno.
    rankDiff = 0

    # Se obtiene el rango de la matriz de coeficientes.
    coRank = matrixRank (coMatrix)

    # Se obtiene el rango de la matriz aumentada.
    augMatrixRank = matrixRank (augMatrix)

    # Si el rango de las matrices no es igual:
    if (coRank != augMatrixRank):
        # El sistema es incompatible.
        eqSysType = 0

    # En caso contrario:
    else:
        # Si el rango de las matrices es menor que el número de incógnitas:
        if (coRank < nParams):
            # El sistema es compatible indeterminado.
            eqSysType = 1

        # Si el rango de las matrices es igual o mayor que el número de incógnitas:
        else:
            # El sistema es compatible determinado.
            eqSysType = 2

            # Si el sistema tiene un rango mayor que su número de incógnitas:
            if (coRank > nParams):
                # Se calcula la diferencia y se asigna a la variable rankDiff.
                rankDiff = coRank - nParams

    # Devuelve el tipo de sistema de ecuaciones y la diferencia entre el rango y el número de parámetros en caso de haber más ecuaciones que parámetros.
    return eqSysType, rankDiff

# Función exportEquationSystemList
# Esta función es el analogo del modo ecuacional de la función exportMatrixList.
# El propósito de esta función es exportar los sistemas de ecuaciones lineales, sus tipos y sus soluciones (en caso de ser compatible determinado)
# al archivo de salida que corresponda según lo especificado en la opción 'path'.
def exportEquationSystemList (eqSysList, solutionList):
    # Se establece la ruta del archivo de salida como la ruta del archivo especificado en la opción 'path' más la extensión '.output'.
    path = config ['path'] + '.output'

    # Crea el archivo de salida.
    createOutputFile (path)

    # Abre el archivo de salida para escribir los sistemas de ecuaciones lineales en él.
    # Lo abre como un archivo codificado en unicode para escribir carácteres como α, β y ω.
    outputFile = open (path, 'a', encoding = 'utf-8')

    # Se escriben todos los sistemas de ecuaciones lineales en el archivo.

    # Por cada sistema:
    for eqSys in range (len (eqSysList)):
        # Si no es el primer sistema de ecuaciones:
        if (eqSys != 0):
            # Añade dos líneas en blanco.
            outputFile.write ('\n\n\n')

        # Se escribe un título para el sistema de ecuaciones, pero convirtíendo el número del ecuaciones de índice 0 a índice 1.
        outputFile.write ('Sistema de ecuaciones lineales ' + str (eqSys + 1) + ':')

        # Se escribe el sistema de ecuaciones, para ello se usan la lista de incógnitas y la matriz que representa el sistema de ecuaciones.
        outputFile.write ('\n\n' + matrixToEquationSystem (eqSysList [eqSys] [0], transposeMatrix (eqSysList [eqSys] [1], len (eqSysList [eqSys] [1]), len (eqSysList [eqSys] [1] [0]))))

        # Si el primer elemento en la lista de soluciones del sistema es 0:
        if (solutionList [eqSys] [0] == 0):
            # El sistema es incompatible.
            outputFile.write ('\n\n  Sistema incompatible.')

        # Si es 1:
        elif (solutionList [eqSys] [0] == 1):
            # El sistema es compatible indeterminado.
            outputFile.write ('\n\n  Sistema compatible indeterminado.')

        # Si es 2:
        else:
            # El sistema es compatible determinado.
            outputFile.write ('\n\n  Sistema compatible determinado.')

            # Como en este caso hay soluciones concretas, se escriben:
            outputFile.write (parseSolutionList (solutionList  [eqSys] [1], solutionList [eqSys] [2]))

    # Cierra el archivo de salida.
    outputFile.close ()

# Función matrixToEquationSystem
# Genera una cadena de carácteres que contiene el sistema de ecuaciones en cuestión a partir de la matriz que lo representa y la lista de parámetros del sistema.
# Se crea a partir de la matriz aumentada que lo representa porque así se puede "arreglar" el formato del sistema introducido.
# Por ejemplo, "4y  - -3z" puede convertirse a "4y + 3z".
def matrixToEquationSystem (paramList, matrix):
    # Se inicializa el string que contiene el sistema de ecuaciones lineales como un string vacío.
    eqSys = ''

    # Por cada fila de la matriz, es decir, cada ecuación:
    for equation in range (len (matrix)):
        # Si el sistema de ecuaciones solo tiene una ecuación:
        if (len (matrix) == 1):
            # Se añaden una llave y la ecuación convertida a string.
            eqSys += '  { ' + equationToStr (matrix [equation], paramList)

        # Si el sistema de ecuaciones tiene más de una ecuación:
        else:
            # Si la ecuación es la primera:
            if (equation == 0):
                # Se añaden al string un tabulado de dos espacios, la parte superior de la llave,
                # la ecuación y un lateral de la llave en una nueva línea.
                eqSys += '  ⎛ ' + equationToStr (matrix [equation], paramList) + '\n  ⎢\n'

            # Si la ecuación es la última:
            elif (equation == len (matrix) - 1):
                # Se añade al string lo mismo que en el caso de la primera,
                # pero cambiando la parte superior de la llave por la parte inferior y no añadiendo la nueva línea y su contenido.
                eqSys += '  ⎝ ' + equationToStr (matrix [equation], paramList)

            # Si la ecuación no es ni la primera ni la última:
            else:
                # Si el número de ecuaciones es par:
                if (len (matrix) % 2 == 0):
                    # Si la ecuación es la última de la primera mitad de ecuaciones:
                    if (equation == (len (paramList) / 2) - 1):
                        # Se añade lo de siempre, pero con un lateral de llave al principio y el centro de la llave en la nueva línea.
                        eqSys += '  ⎢ ' + equationToStr (matrix [equation], paramList) + '\n  ⎨\n'

                    # En caso contrario:
                    else:
                        # Se añade lo mismo, pero en vez de añadir un centro de llave en la nueva línea se añade un lateral.
                        eqSys += '  ⎢ ' + equationToStr (matrix [equation], paramList) + '\n  ⎢\n'

                # Si el número de ecuaciones es impar:
                else:
                    # Si la variable es la del medio de la lista de variables:
                    if (equation == (len (matrix) - 1) / 2):
                        # Se añade lo de siempre, pero con un centro de llave al principio.
                        eqSys += '  ⎨ ' + equationToStr (matrix [equation], paramList) + '\n  ⎢\n'

                    # En caso contrario:
                    else:
                        # Se añade lo mismo que en su análogo par (tabulado + lateral + contenido + nueva línea con tabulado y lateral).
                        eqSys += '  ⎢ ' + equationToStr (matrix [equation], paramList) + '\n  ⎢\n'

    # Devuelve la cadena de carácteres en la que está contenido el sistema de ecuaciones.
    return eqSys

# Función equationToStr
# Convierte una fila de la matriz aumentada que representa el sistema de ecuaciones en una ecuación tipada como string.
def equationToStr (row, paramList):
    # Se declara el string que contiene la ecuación como un string vacío.
    equation = ''

    # Se declara una variable que actúa como indicador de si debe quitarse el signo de suma o resta al principio.
    # Esto pasa cuando el cociente de la primera incógnita es 0.
    # Por defecto, se presupone que este no es el caso.
    noSignAtBeginning = False

    # Por cada elemento de la fila:
    for rowe in range (len (row)):
        # Solo se añade el elemento a la ecuación si no es 0 (0x = 0 y como 0 es el elemento neutro de la suma y resta pues sería como no hacer nada).
        # A no ser que sea una solución de ecuación, es decir, el último elemento de la fila.
        if (row [rowe] != 0 or (row [rowe] == 0 and rowe == len (row) - 1)):
            # Si el elemento es el primero de la fila:
            if (rowe == 0):
                # Si es un número negativo:
                if (row [rowe] < 0):
                    # Si su valor absoluto es 1:
                    if (abs (fracToFloat (row [rowe])) == 1):
                        # Se añaden el signo negativo y la variable de la que es coeficiente el elemento.
                        equation += '-' + paramList [rowe]

                    # Si su valor absoluto no es 1:
                    else:
                        # Se añaden el signo negativo, el valor absoluto del elemento y la variable de la que es coeficiente.
                        equation += '-' + str (abs (fracToFloat (row [rowe]))) + paramList [rowe]

                # Si es un numero positivo:
                else:
                    # Si su valor absoluto es 1:
                    if (abs (fracToFloat (row [rowe])) == 1):
                        # Se añade la variable de la que es coeficiente el elemento.
                        equation += paramList [rowe]

                    # Si su valor absoluto no es 1:
                    else:
                        # Se añaden el elemento y la variable de la que es coeficiente.
                        equation += str (fracToFloat (row [rowe])) + paramList [rowe]

            # Si el elemento es el último de la fila:
            elif (rowe == len (row) - 1):
                # Es una constante, así que se añade la parte derecha de la ecuación: el signo de igual separado por espacios y el valor.
                equation += ' = ' + str (fracToFloat (row [rowe]))

            # Si el elemento no es ni el último ni el primero de la fila:
            else:
                # Si es un número negativo:
                if (row [rowe] < 0):
                    # Si el indicador noSignAtBeginning está desactivado:
                    if (not noSignAtBeginning):
                        # Se añade el signo de resta.
                        equation += ' - '

                    # Si está activado:
                    else:
                        # No se añade el signo de resta.

                        # Se desactiva.
                        noSignAtBeginning = False

                    # Si su valor absoluto es 1:
                    if (abs (fracToFloat (row [rowe])) == 1):
                        # Se añaden el signo negativo separado por espacios y la variable de la que es coeficiente el elemento.
                        equation += paramList [rowe]

                    # Si su valor absoluto no es 1:
                    else:
                        # Se añaden el signo negativo separado por espacios, el valor absoluto del elemento y la variable de la que es coeficiente.
                        equation += str (abs (fracToFloat (row [rowe]))) + paramList [rowe]

                # Si es un número positivo:
                else:
                    # Si el indicador noSignAtBeginning está desactivado:
                    if (not noSignAtBeginning):
                        # Se añade el signo de suma.
                        equation += ' + '

                    else:
                        # No se añade el signo de suma.

                        # Se desactiva.
                        noSignAtBeginning = False

                    # Si su valor absoluto es 1:
                    if (abs (fracToFloat (row [rowe])) == 1):
                        # Se añaden el signo positivo separado por espacios y la variable de la que es coeficiente el elemento.
                        equation += paramList [rowe]

                    # Si su valor absoluto no es 1:
                    else:
                        # Se añaden el signo positivo separado por espacios, el valor absoluto del elemento y la variable de la que es coeficiente.
                        equation += str (abs (fracToFloat (row [rowe]))) + paramList [rowe]

        # Si el elemento no es una solución de ecuación, es decir, es coeficiente de una incógnita y es 0:
        else:
            # Se establece que no debe haber signo al principio.
            noSignAtBeginning = True

    # Como puede verse, se ha intentado que todos los valores sean convertidos a enteros si es que su parte decimal equivale a 0.

    # Devuelve la ecuación en forma de string.
    return equation

# Función parseSolutionList
# En caso de ser un sistema compatible determinado, pasa las soluciones del sistema de ecuaciones a cadena de carácteres
# encapsuladas por la izquierda con una "llave gigante".
def parseSolutionList (paramList, solutions):
    # Se inicializa el string que contiene las soluciones del sistema de ecuaciones con el título.
    solutionStr = '\n\n  Soluciones:\n'

    # Por cada incógnita en la lista de incógnitas:
    for variable in range (len (paramList)):
        # Si el sistema solo tiene una incógnita:
        if (len (paramList) == 1):
            # Se añaden al string un tabulado de dos espacios, una llave y la variable en cuestión con su valor.
            solutionStr += '  { ' + paramList [variable] + ' = ' +  str (fracToFloat (solutions [variable]))

        # Si el sistema tiene más de una incógnita:
        else:
            # Si la incógnita es la primera:
            if (variable == 0):
                # Se añaden al string un tabulado de dos espacios, la parte superior de la llave,
                # la variable con su valor y un lateral de la llave en una nueva línea.
                solutionStr += '  ⎛ ' + paramList [variable] + ' = ' +  str (fracToFloat (solutions [variable])) + '\n  ⎢\n'

            # Si la incógnita es la última:
            elif (variable == len (paramList) - 1):
                # Se añade al string lo mismo que en el caso de la primera,
                # pero cambiando la parte superior de la llave por la parte inferior y no añadiendo la nueva línea y su contenido.
                solutionStr += '  ⎝ ' + paramList [variable] + ' = ' +  str (fracToFloat (solutions [variable]))

            # Si la incógnita no es ni la primera ni la última:
            else:
                # Si el número de variables es par:
                if (len (paramList) % 2 == 0):
                    # Si la variable es última de la primera mitad de variables:
                    if (variable == (len (paramList) / 2) - 1):
                        # Se añade lo de siempre, pero con un lateral de llave al principio y el centro de la llave en la nueva línea.
                        solutionStr += '  ⎢ ' + paramList [variable] + ' = ' +  str (fracToFloat (solutions [variable])) + '\n  ⎨\n'

                    # En caso contrario:
                    else:
                        # Se añade lo mismo, pero en vez de añadir un centro de llave en la nueva línea se añade un lateral.
                        solutionStr += '  ⎢ ' + paramList [variable] + ' = ' +  str (fracToFloat (solutions [variable])) + '\n  ⎢\n'

                # Si el número de variables es impar:
                else:
                    # Si la variable es la del medio de la lista de variables:
                    if (variable == (len (paramList) - 1) / 2):
                        # Se añade lo de siempre, pero con un centro de llave al principio.
                        solutionStr += '  ⎨ ' + paramList [variable] + ' = ' +  str (fracToFloat (solutions [variable])) + '\n  ⎢\n'

                    # En caso contrario:
                    else:
                        # Se añade lo mismo que en su análogo par (tabulado + lateral + contenido + nueva línea con tabulado y lateral).
                        solutionStr += '  ⎢ ' + paramList [variable] + ' = ' +  str (fracToFloat (solutions [variable])) + '\n  ⎢\n'

    # Devuelve la cadena de carácteres en la están contenidos los valores de las variables en un formato más legible.
    return solutionStr

# Función matrixToString
# Función que permite convertir matrices en cadenas de carácteres cuya manera de ser representadas depende del formato especificado en la opción 'style'.
# También sirve para representar los factores en la tabla de operaciones como enteros en la medida de lo posible,
# ya que la tabla de operaciones no deja de ser un array bidimensional que simula ser una matriz irregular.
def matrixToString (matrix, style):
    # Se inicia la matriz en formato de cadena de carácteres como un string vacío.
    matrixStr = ''

    # Si se quiere exportar al tipo de estilo 1:
    if (style == '1' or style == 'py' or style == 'python' or style == 'plain'):
        # La matriz se deja exactamente igual, es decir, como un array bidimensional de Python.
        # También se añade un espacio a la izquierda.
        matrixStr = ' ' + str (matrix)

    # Si se quiere exportar al tipo de estilo 2:
    if (style == '2' or style == 'wa' or style == 'wolfram'):
        # Las matrices en formato Wolfram son prácticamente idénticas a las matrices en formato Python, excepto por un pequeño detalle:
        # los corchetes ([]) se sustituyen por llaves ({}).
        # De hecho, las matrices con corchetes también pueden ser introducidas en WolframAlpha sin problema alguno.
        # Sin embargo, a la hora de usar el kernel de Wolfram Mathematica no se admiten los corchetes.

        # Se añade una llave de apertura al string (con un espacio a la izquierda).
        matrixStr += ' {'

        # Por cada fila:
        for row in range (len (matrix)):
            # Se añade una llave de apertura.
            matrixStr += '{'

            # Por cada elemento de la fila:
            for rowe in range (len (matrix [row])):
                # Se añade el elemento en forma de string.
                matrixStr += str (matrix [row] [rowe])

                # También se añaden una coma y un espacio como separador siempre y cuando el elemento no sea el último de la fila:
                if (rowe < len (matrix [row]) - 1):
                    matrixStr += ', '

            # Se añade una llave de clausura.
            matrixStr += '}'

            # También se añaden una coma y un espacio como separador siempre y cuando el elemento no sea el último de la fila:
            if (row < len (matrix) - 1):
                matrixStr += ', '

        # Se añade una llave de clausura al string.
        matrixStr += '}'

    # Si se quiere exportar al tipo de estilo 3:
    if (style == '3' or style == 'default' or style == 'human'):
        # Las matrices exportadas al modo human tienen la particularidad de ser bastante más difíciles de exportar para el programa
        # pero son mucho más agradables a la vista para los usuarios,
        # ya que los elementos están repartidos en filas y columnas que están centradas (más o menos).

        # Se inicializa la lista en la que estarán incluidas las filas convertidas a strings.
        rowStrList = []

        # Se asume que la fila más larga (como string) es la primera.
        largestRow = 0

        # Se analiza cada fila.
        for row in range (len (matrix)):
            # Si es un string más largo que la considerada como la más larga:
            if (len (str (matrix [row])) > len (str (matrix [largestRow]))):
                # Ahora esta será la más larga.
                largestRow = row

        # Se analiza cada fila.
        for row in range (len (matrix)):
            # Se declara la fila en formato de string como un string vacío.
            rowStr = ''

            # Se analiza el cada elemento de la fila.
            for rowe in range (len (matrix [row])):
                # Si el elemento es un string más corto que su análogo de la fila más larga:
                if (len (str (matrix [row] [rowe])) < len (str (matrix [largestRow] [rowe]))):
                    # Se justifica el elemento a la izquierda y se añade al string de la fila.
                    rowStr += (str (matrix [row] [rowe])).ljust (len (str (matrix [largestRow] [rowe])), ' ')

                # Si el elemento es igual de largo que su análogo de la fila más larga:
                elif (len (str (matrix [row] [rowe])) == len (str (matrix [largestRow] [rowe]))):
                    # Se añade al string de la fila.
                    rowStr += str (matrix [row] [rowe])

                # Si el elemento es más largo que su análogo de la fila más larga:
                elif (len (str (matrix [row] [rowe])) > len (str (matrix [largestRow] [rowe]))):
                    # Se justifica el elemento a la derecha y se añade al string de la fila.
                    rowStr += (str (matrix [row] [rowe])).rjust (len (str (matrix [largestRow] [rowe])), ' ')

                # Si el elemento no es el último de la fila:
                if (rowe < len (matrix [row]) - 1):
                    # Se añade un separador que consiste en tres espacios.
                    rowStr += '   '

            # Se añade el string de la fila a la lista de strings de filas.
            rowStrList.append (rowStr)

        # Se inicializa el espacio en blanco que hay sobre la primera y debajo de la última fila como un string vacío.
        spaceStr = ''

        # Se asume que la fila que es un string más largo es la primera.
        largestRowStr = 0

        # Se mira cada fila:
        for rowStr in range (len (rowStrList)):
            # Si es más larga como string que la fila anteriormente considerada como la más larga:
            if (len (rowStrList [rowStr]) > len (rowStrList [largestRowStr])):
                # Pasa a ser la más larga.
                largestRowStr = rowStr

        # Se añade un número de espacios equivalente a la longitud de la fila más larga más dos carácteres: un espacio al principio y otro al final.
        for spaceCharacter in range (len (rowStrList [largestRowStr])+ 2):
            spaceStr += ' '

        # Antes de añadir las filas, se añaden las parte superiores de ambos "corchetes gigantes" de la matriz,
        # que estarán separador por un número de espacios equivalente a la fila más larga con un margen al principio y al final de un espacio.
        matrixStr += '\n    ┌' + spaceStr + '┐\n'

        # Se analiza cada string de fila.
        for rowStr in range (len (rowStrList)):
            # Se añade la parte izquierda del corchete más un tabulado de cuatro espacios.
            matrixStr += '    │ '

            # Se centra el string comparándolo a la fila más larga y se añade al string de la matriz.
            matrixStr += (rowStrList [rowStr]).center (len (rowStrList [largestRowStr]), ' ')

            # Se añade la parte derecha del corchete y se salta de línea.
            matrixStr += ' │\n'

        # Una vez añadidas todas las filas, se cierran los corchetes añadiendo sus partes inferiores separadas por espacio anteriormente mencionado.
        matrixStr += '    └' + spaceStr + '┘'

    # Devuelve la matriz convertida a string, sea cual sea el estilo elegido.
    return matrixStr

# Función prettifyMatrixElements
# Convierte todos los elementos que se puedan de la matriz de números flotantes a enteros y redondea los números decimales a 6 decimales
# (o el número de decimales que se quiera cambiando la variable 'decimals' de más abajo).
# No es por ninguna razón práctica, solo estética ya que tener .0 como parte decimal o muchos decimales me parece saturante a la hora de observar los resultados.
# También sirve para la tabla de operaciones, que al fin y al cabo no deja de ser una matriz irregular.
def prettifyMatrixElements (matrix):
    # Se establece el número de decimales a redondear.
    decimals = 6

    # Por cada fila de la matriz:
    for row in range (len (matrix)):
        # Mira cada elemento.
        for rowe in range (len (matrix [row])):
            # Si el elemento es en realidad un entero que está tipado como un número flotante, lo convierte a entero y lo sustituye en la matriz.
            # Si no, lo redondea a los decimales elegidos.
            matrix [row] [rowe] = round (fracToFloat (matrix [row] [rowe]), decimals)

    # Devuelve la matriz con todos los cambios que se le hayan aplicado.
    return matrix

# Función fracToFloat
# Esta función sirve para convertir fracciones tipadas como strings, números flotantes o números enteros
# a números flotantes (y enteros) como puede ser convertir '10/2.5' en 4.
# También convierte productos: por ejemplo, '1*2' pasaría a ser símplemente 2.
# Además, también sirve para convertir fracciones como es el caso '1296^2^0.25^0.5^1^2^0.5' -> 6.
# Obviamente, si el número introducido no es una fracción lo deja como está y lo intenta convertir a entero.
# 
# Soy consciente de que podría usar el módulo Fraction pero por cómo he diseñado el programa (sobre todo el mecanismo de parseo de los sistemas de ecuaciones y matrices),
# me parece mejor usar este método que he visto en Stack Overflow (https://stackoverflow.com/a/30629776) y que he adaptado a mis necesidades.
def fracToFloat (fraction):
    # Se convierte el elemento a analizar en un string.
    # Esto es útil para analizar luego cada uno de sus carácteres.
    fraction = str (fraction)

    # Si hay comas se sustituyen por puntos. Esto es por si el usuario usa comas para expresar los decimales.
    if (',' in fraction):
        fraction = fraction.replace (',', '.')

    # Se eliminan los paréntesis si es que los hay, ya que como explico en la documentación
    # solo se admiten los signos de adición y substracción, los operadores de división (/) y multiplicación (*) y el exponente (^).
    if ('(' in fraction):
        fraction = fraction.replace ('(', '')

    if (')' in fraction):
        fraction = fraction.replace (')', '')

    # Comprueba si el string introducido puede convertirse a flotante.
    # Si se puede, no hace falta hacer nada más: se devuelve el número convertido de string a flotante (o a entero si se puede).
    try:
        return floatToInt (float (fraction))

    # Si no se puede:
    except ValueError:
        # Se asume por defecto que todos los carácteres son válidos.
        allCharsValid = True

        # Se analiza cada carácter en la fracción.
        for char in fraction:
            # Se comprueba si el carácter puede ser convertido a número.
            try:
                float (char)

            # Si no es un número:
            except:
                # Si el carácter no es uno de los carácteres especiales permitidos:
                if (char not in '-+./*()^'):
                    # Se establece que no todos los carácteres son válidos.
                    allCharsValid = False

        # Si todos los carácteres son válidos:
        if (allCharsValid):
            # Se establece un indicador de negatividad que estará desactivado por defecto.
            negativeNumber = False

            # Se separan el numerador y el denominador de la fracción, que están cada uno a un lado de la barra.
            operandList = fraction.split ('/')

            # Por cada operando en la lista de operandos:
            for operand in range (len (operandList)):
                # Se analiza cada carácter:
                for char in operandList [operand]:
                    # Si el carácter es el signo positivo:
                    if (char == '+'):
                        # No se invierte el signo del número.

                        # Se quita el carácter del elemento.
                        operandList [operand] = operandList [operand].replace (char, '', 1)

                    # Si el carácter es el signo negativo:
                    elif (char == '-'):
                        # Se invierte el signo del número.

                        # Si el número es positivo:
                        if (not negativeNumber):
                            # Pasa a ser negativo.
                            negativeNumber = True

                        # Si el número es negativo:
                        else:
                            # Pasa a ser positivo.
                            negativeNumber = False

                        # Se quita el carácter del elemento.
                        operandList [operand] = operandList [operand].replace (char, '', 1)

                # Si contiene el operador de potencia (^):
                if ('^' in str (operandList [operand])):
                    # Se separan los factores (los elementos que se están multiplicando) en función del operador.
                    powerList = operandList [operand].split ('^')

                    # Se declara una variable que representa el operador después de elevarlo a la potencia que se haya especificado.
                    # Es equivalente al primer elemento del operando.
                    newOperand = fracToFloat (powerList [0])

                    # Se elimina el primer elemento de la lista.
                    powerList.pop (0)

                    # Se declara una variable que representa el número al que se elevará el operador.
                    # Es equivalente al ahora primer elemento del operando.
                    totalPower = fracToFloat (powerList [0])

                    # Se elimina el primer elemento de la lista.
                    powerList.pop (0)

                    # Si la lista no está vacía después de quitarle los dos primeros elementos, es que sigue habiendo exponentes.
                    if (powerList != None):
                        # Para simular un bucle do-while:

                        # Se declara una variable que indica si el bucle debe seguir.
                        # Se establece en True para que se ejecute el bucle de primeras.
                        shouldRestart = True

                        # El bucle se ejecuta mientras la variable shouldRestart sea True.
                        while (shouldRestart):

                            # Se establece que el bucle no debe reiniciarse.
                            shouldRestart = False

                            # Por cada potencia en la lista de potencias:
                            for power in range (len (powerList)):
                                # Se multiplica el número al que se eleva por la potencia.
                                # Esto es debido a las leyes de la exponenciación: ((2^2)^2)^2 = 2^(2*2*2) = 2^8 = 256
                                totalPower *= fracToFloat (powerList [power])

                                # Se elimina la potencia de la lista de potencias.
                                powerList.pop (power)

                                # Se establece que el bucle debe reiniciarse y se para el proceso para reiniciarlo.
                                shouldRestart = True
                                break

                    # Se crea el nuevo operando elevando el primer valor de la expresión de exponenciación a la "acumulación" de exponentes.
                    newOperand = pow (newOperand, totalPower)

                    # El operando ahora será el resultado de realizar la operación de elevar el primer número al resto.
                    operandList [operand] = newOperand

                # Si contiene el operador de multiplicación (*):
                if ('*' in str (operandList [operand])):
                    # Se declara una variable que representa el valor del operando convertido a número.
                    # Se le da el valor de 1 porque es el elemento neutro de la multiplicación.
                    newOperand = 1

                    # Se separan los factores (los elementos que se están multiplicando) en función del operador de producto.
                    factorList = operandList [operand].split ('*')

                    # Por cada factor:
                    for factor in factorList:
                        # Se multiplica el nuevo operando por el factor.
                        # La función se vuelve a llamar a sí misma por si hace falta convertir el factor.
                        newOperand *= fracToFloat (factor)

                    # El operando ahora será el resultado de la multiplicación de sus elementos internos.
                    operandList [operand] = newOperand

            # Como pasaba con la multiplicación, se declara una variable que representa el denominador de la división.
            # Como 1 es el elemento neutro de la división, se le da este valor a la variable.
            denominator = 1

            # Si la lista de operandos tiene más de un operando:
            if (len (operandList) > 1):
                # Se analiza cada operando:
                for operand in range (len (operandList)):
                    # Si el operando no es el primero:
                    if (operand != 0):
                        # Se multiplica el denominador por el operando, que pasa por la función para ver si es un número o hace falta convertirlo.
                        denominator *= fracToFloat (operandList [operand])

            # Por último, se divide el primer elemento de la lista (el numerador) entre el resto (el denominador).
            fraction = float (fracToFloat (operandList [0])) / denominator

            # Una vez terminado todo el proceso, convierte el número flotante obtenido a entero.
            # Así evitamos tener que llamar a la función fracToInt para analizar el resultado de la función fracToFloat,
            # ya que ahora irá implícito el proceso fracción?/multiplicación? -> flotante -> entero? (? = si es que lo es).
            fraction = floatToInt (fraction)

            # Si está activado el indicador de negatividad del número:
            if (negativeNumber):
                # Se cambia el signo del número.
                fraction = -fraction

                # Se desactiva el indicador de negatividad.
                negativeNumber = False

        # Si la expresión introducida era válida, la devuelve como un número flotante (o entero).
        # Si no lo era, devuelve la misma expresión.
        return fraction

# Función fracToFloat
# Analiza un número y comprueba los siguiente:
# - 1: Si su parte decimal es 0.9.... (que equivale a 1) o 0.0...1 (que equivale a 0).
#      Si es así, cambia el número al entero al que equivale (explicado más adelante).
# - 2: Si su parte decimal equivale a 0.
#      En este caso, convierte el número a entero.
def floatToInt (number):
    # Si el valor absoluto de la parte decimal del número es 0.9... (se puede ajustar el número de nueves para añadir o restar precisión):
    if (abs (math.modf (number) [0]) >= 0.99999):
        # Si el numero es negativo:
        if (number < 0):
            # Lo convierte a entero y le resta 1.
            number = int (number) - 1

        # Si el número es positivo:
        if (number > 0):
            # Lo convierte a entero y le suma 1.
            number = int (number) + 1

    # Si el valor absoluto de la parte decimal del número es 0.0...1 (se puede ajustar el número de ceros para añadir o restar precisión):
    if (abs (math.modf (number) [0]) <= 0.00001):
        # Convierte el número en entero.
        number = int (number)

    # Si la parte decimal del número es 0:
    if (math.modf (number) [0] == 0):
        # Convierte el número en entero.
        number = int (number)

    # Devuelve el número, cambiado o no.
    return number

# Función mainMenu
# Genera un menú de bienvenida para la versión Prog.
def mainMenu ():
    # El nombre, título y subtítulo del programa.
    name = 'SimpleGauss'
    title = 'Inversor de matrices y solucionador de sistemas lineales'
    subtitle = 'Por Mikel Pintado'

    # Se obtiene la longitud del título para centrar el resto de elementos del menú en función del título.
    titleLength = len (title)

    # Se centran el subtítulo y el nombre del programa en función del título.
    subtitle = subtitle.center (titleLength + 2)
    name = name.center (titleLength + 2)

    # Se inicia la fecha en formato "español" (hora:minuto:segundo día/mes/año).
    executionDateMenu = ''

    # Se divide la fecha en dos secciones en función de la barra baja: la hora y el día.
    dateSectionList = executionDate.split ('_')

    # Por cada sección empezando por atrás:
    for dateSection in range (-1, 1):
        # Si la sección es la hora (índice -1):
        if (dateSection == -1):
            # Se dividen sus elementos en función del guión.
            hourElementList = dateSectionList [dateSection].split ('-')

            # Por cada elemento:
            for hourElement in range (3):
                # Se añade al string de la fecha.
                executionDateMenu += hourElementList [hourElement]

                # Si no es el último:
                if (hourElement != 2):
                    # Se añaden dos puntos para separarlo del siguiente.
                    executionDateMenu += ':'

                # Si es el último:
                else:
                    # Se añade un espacio para separar la hora de la fecha.
                    executionDateMenu += ' '

        # Si la sección es la hora (índice 0):
        else:
            # Se dividen sus elementos en función del guión.
            dayElementList = dateSectionList [dateSection].split ('-')

            # Por cada elemento iterando la lista al revés (para pasar la fecha del formato año/mes/día al formato día/mes/año):
            for dayElement in range (2, -1, -1):
                # Se añade al string de la fecha.
                executionDateMenu += dayElementList [dayElement]

                # Si el elemento no es el año (índice 0):
                if (dayElement != 0):
                    # Se añade una barra inclinada para separarlo del siguiente.
                    executionDateMenu += '/'

    # Se centra la fecha en función del menú.
    executionDateMenu = executionDateMenu.center (titleLength + 2)

    # Se declaran un string de espacios que sirve para separar el título y el subtítulo
    # y un string de borde de tabla para separar las secciones del menú, ambos centrados respecto al título.
    spaceStr = ''.center (titleLength + 2)
    separatorStr = ''.center (titleLength + 2, '─')

    # Se genera un menú que consiste en dos secciones (título y subtítulo; y fecha y hora) encapsuladas en una caja.
    menuStr = '┌' + separatorStr + '┐\n'
    menuStr += '│' + name + '│\n'
    menuStr += '├' + separatorStr + '┤\n'
    menuStr += '│ ' + title + ' │\n'
    menuStr += '│' + spaceStr + '│\n'
    menuStr += '│' + subtitle + '│\n'
    menuStr += '├' + separatorStr + '┤\n'
    menuStr += '│' + executionDateMenu + '│\n'
    menuStr += '├' + separatorStr + '┤\n'

    # Se concatena otra caja que contiene los modos del programa.
    menuStr += '│' + 'Modos disponibles'.center (titleLength + 2) + '│\n'
    menuStr += '│' + ('Matricial (0)'.ljust (int (titleLength / 2) - 1) + ' ' + 'Ecuacional (1)'.rjust (int (titleLength / 2))).center (titleLength + 2) + '│\n'
    menuStr += '└' + separatorStr + '┘\n'

    # Devuelve el string en el que va contenido el menú.
    return menuStr

# Función optionMenu
# Genera un menú en el que se muestran opciones que el usuario puede escoger antes de
# operar con el conjunto de elementos que deben ser analizados, que dependerá del modo de programa que esté en uso.
def optionMenu (mode, paramList, paramPropertyList):
    # Bucle do-while en el que se genera un menú por el que se pregunta al usuario si quiere mostrar la lista de elementos, añadirle un elemento nuevo
    # o eliminar un elemento (siempre que haya más de uno) antes de operar.
    # Para más información sobre los bucles do-while simulados que se usan en este programa, acude a la función fracToFloat.
    shouldRestart = True

    while (shouldRestart):
        # Se limpia la pantalla.
        clearScreen ()

        # Se definen las opciones, que serán strings ajustados en base a la opción más larga: la opción 1 (mostrar el conjunto de elementos).

        # Si el programa está en modo matricial (modo 0):
        if (mode == 0):
            option1 = 'Mostrar la lista de matrices (1)'
            option1Length = len (option1)

            option2 = 'Añadir una nueva matriz (2)'.ljust (option1Length)
            option3 = 'Eliminar una matriz (3)'.ljust (option1Length)

        # Si el programa está en modo ecuacional (modo 1):
        else:
            option1 = 'Mostrar la lista de sistemas de ecuaciones (1)'
            option1Length = len (option1)

            option2 = 'Añadir un nuevo sistema de ecuaciones (2)'.ljust (option1Length)
            option3 = 'Eliminar un sistema de ecuaciones (3)'.ljust (option1Length)

        option4 = 'No hacer nada (Enter)'.ljust (option1Length)

        # Se centra el título en base a la longitud de la primera opción.
        title = 'Opciones disponibles'.center (option1Length)

        # Se declaran un string de espacios que sirve para separar las opciones entre ellas
        # y un string de borde de tabla para separar las secciones del menú, ambos centrados respecto a la primera opción.
        spaceStr = ''.center (option1Length + 2)
        separatorStr = ''.center (option1Length + 2, '─')

        # Se genera una caja que contiene las opciones.
        menuStr = '┌' + separatorStr + '┐\n'
        menuStr += '│ ' + title + ' │\n'
        menuStr += '├' + separatorStr + '┤\n'
        menuStr += '│ ' + option1 + ' │\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│ ' + option2 + ' │\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│ ' + option3 + ' │\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│ ' + option4 + ' │\n'
        menuStr += '└' + separatorStr + '┘\n'

        # Se imprime el menú.
        print (menuStr)

        # Se pide al usuario que introduzca una opción.
        option = input ('>>> ')

        # Si el usuario ha elegido mostrar la lista de elementos:
        if (option == '1'):
            # Limpia la pantalla
            clearScreen ()

            # Si el programa está en modo matricial (modo 0):
            if (mode == 0):
                # Por cada matriz en la lista:
                for matrix in range (len (paramList)):
                    # Si no es la primera matriz:
                    if (matrix != 0):
                        # Añade dos líneas en blanco.
                        print ('\n\n')

                    # Imprime su índice.
                    print ('Matriz ' + str (matrix + 1) + ':')

                    # La muestra en pantalla, de la misma manera que en la función exportMatrixList,
                    # pero siempre con el estilo 'default' y con los elementos convertidos a números en la medida de lo posible.
                    # Para ello, se aprovecha la primera salida de la función checkIfSquared.
                    print (matrixToString (checkIfSquared (paramList [matrix]) [0], 'default'))

            # Si el programa está en modo ecuacional (modo 1):
            else:
                # Por cada sistema de ecuaciones en la lista:
                for eqSys in range (len (paramList)):
                    # Si no es el primer sistema de ecuaciones:
                    if (eqSys != 0):
                        # Añade dos líneas en blanco.
                        print ('\n\n')

                    # Imprime su índice.
                    print ('Sistema de ecuaciones lineales ' + str (eqSys + 1) + ':')

                    # Lo muestra en pantalla, de la misma manera que en la función exportEquationSystemList.
                    print (matrixToEquationSystem (paramList [eqSys] [0], transposeMatrix (paramList [eqSys] [1], len (paramList [eqSys] [1]), len (paramList [eqSys] [1] [0]))))

            # Sale del modo de muestreo cuando el usuario pulse Enter.
            input ('\n\nPulsa Enter para continuar.')

        # Si el usuario ha elegido añadir un nuevo elemento a la lista:
        elif (option == '2'):
            # Si el programa está en modo matricial (modo 0):
            if (mode == 0):
                # Se añade la matriz que el usuario introduzca a la lista de elementos.
                paramList.append (inputMatrix ())

            # Si el programa está en modo ecuacional (modo 1):
            else:
                # Se añade el sistema que el usuario introduzca a la lista de elementos.
                paramList.append (inputEquationSystem ())

            # Se añade la entrada que corresponde al nuevo elemento en la lista de propiedades de los elementos.
            paramPropertyList.append ([])

        # Si el usuario ha elegido eliminar un elemento de la lista:
        elif (option == '3'):
            # Limpia la pantalla.
            clearScreen ()

            # Si hay más de un elemento en la lista:
            if (len (paramList) > 1):
                    # Se ejecuta otro bucle do-while en el que se pregunta al usuario el índice (empezando en 1) de la matriz que quiere eliminar.
                    while (shouldRestart):
                        if (mode == 0):
                            # Se pregunta al usuario el índice de la matriz a eliminar.
                            print (f'Introduce el índice de la matriz a eliminar [1-{len (paramList)}] [0 para cancelar]: ', end = '')

                        else:
                            # Se pregunta al usuario el índice del sistema de ecuaciones a eliminar.
                            print (f'Introduce el índice del sistema de ecuaciones lineales a eliminar [1-{len (paramList)}] [0 para cancelar]: ', end = '')

                        # Se almacena la respuesta del usuario.
                        elementToRemove = input ()

                        # Se intenta convertir la respuesta del usuario a un número entero o flotante.
                        try:
                            elementToRemove = fracToFloat (elementToRemove)

                        # Se haya podido o no:
                        finally:
                            # Si la respuesta del usuario es un número entero igual o mayor que 1 y menor o igual que la longitud de la lista de elementos:
                            if (type (elementToRemove) == int and (elementToRemove >= 1 and elementToRemove <= len (paramList))):
                                # Se elimina el elemento de la lista (con índice 0, de ahí el -1).
                                paramList.pop (elementToRemove - 1)

                                # Se eliminina su entrada de la lista de propiedades.
                                paramPropertyList.pop (elementToRemove - 1)

                                # No se reinicia el bucle para preguntar al usuario el índice del elemento.
                                shouldRestart = False

                            # Si el índice del elemento a eliminar que ha introducido el usuario es 0:
                            elif (elementToRemove == 0):
                                # Se sale del bucle.
                                shouldRestart = False

                            # En caso contrario, se le vuelve a preguntar al usuario por un número válido.

                    # Se devuelve a la variable shouldRestart a su estado anterior para que no afecte al otro bucle.
                    shouldRestart = True

            # Si no hay más de un elemento en la lista, se avisa al usuario de que no puede eliminar más elementos de la listas:
            else:
                # Si el programa está en modo matricial:
                if (mode == 0):
                    input ('No se pueden eliminar más matrices de la lista.')

                else:
                    input ('No se pueden eliminar más sistemas lineales de la lista.')

                # Se sale del aviso de error cuando el usuario pulse Enter.
                input ('\nPulsa Enter para continuar.')

        # Si el usuario ha elegido no hacer nada más:
        elif (option == ''):
            # No se vuelve a ejecutar el bucle.
            shouldRestart = False

        # Si la opción introducida no es válida, se vuelve al menú.

    # Devuelve la lista de parámetros y la lista de propiedades de parámetros hayan sido cambiadas o no.
    # En el caso del modo matricial, la lista de parámetros es la lista de matrices y la lista de propiedades de parámetros es la lista de propiedades de las matrices.
    # En el caso del modo ecuacional, lo son la lista de sistemas de ecuaciones lineales y la lista de soluciones.
    return paramList, paramPropertyList

# Función matrixOptionMenu
# Genera un menú en el que se muestran opciones que el usuario puede escoger para mostrar ciertas características de las matrices analizadas.
def matrixOptionMenu (propertyList):
    # Bucle do-while en el que se genera un menú por el que se pregunta al usuario si quiere mostrar todas las matrices que tengan ciertas dimensiones,
    # mostrar la matriz más grande (con más elementos) o calcular la media de los determinantes de las matrices.
    # Para más información sobre los bucles do-while simulados que se usan en este programa, acude a la función fracToFloat.
    shouldRestart = True

    while (shouldRestart):
        # Se limpia la pantalla.
        clearScreen ()

        # Se definen las opciones, que serán strings ajustados en base a la opción más larga: la opción 1 (mostrar las matrices de mxn dimensiones).

        option1 = 'Mostrar todas las matrices de m×n dimensiones (1)'
        option1Length = len (option1)

        option2 = 'Mostrar la matriz más grande (2)'.ljust (option1Length)
        option3 = 'Calcular la media de los determinantes (3)'.ljust (option1Length)
        option4 = 'No hacer nada (Enter)'.ljust (option1Length)

        # Se centra el título en base a la longitud de la primera opción.
        title = 'Opciones disponibles'.center (option1Length)

        # Se declaran un string de espacios que sirve para separar las opciones entre ellas
        # y un string de borde de tabla para separar las secciones del menú, ambos centrados respecto a la primera opción.
        spaceStr = ''.center (option1Length + 2)
        separatorStr = ''.center (option1Length + 2, '─')

        # Se genera una caja que contiene las opciones.
        menuStr = '┌' + separatorStr + '┐\n'
        menuStr += '│ ' + title + ' │\n'
        menuStr += '├' + separatorStr + '┤\n'
        menuStr += '│ ' + option1 + ' │\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│ ' + option2 + ' │\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│ ' + option3 + ' │\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│' + spaceStr + '│\n'
        menuStr += '│ ' + option4 + ' │\n'
        menuStr += '└' + separatorStr + '┘\n'

        # Se imprime el menú.
        print (menuStr)

        # Se pide al usuario que introduzca una opción.
        option = input ('>>> ')

        # Si el usuario ha elegido buscar las matrices de mxn dimensiones:
        if (option == '1'):
            # Se ejecuta otro bucle do-while en el que se pregunta al usuario el número de filas de las matrices que quiere buscar.
            while (shouldRestart):
                # Limpia la pantalla
                clearScreen ()

                # Se almacena la respuesta del usuario.
                dimension1 = input ('Introduce el número de filas de la matriz [0 para cancelar]: ')

                # Se intenta convertir la respuesta del usuario a un número entero o flotante.
                try:
                    dimension1 = fracToFloat (dimension1)

                # Se haya podido o no:
                finally:
                    # Si la respuesta del usuario es un número entero que sea mayor o igual que 0:
                    if (type (dimension1) == int and dimension1 >= 0):
                        # No se reinicia el bucle para preguntar al usuario el número de filas.
                        shouldRestart = False

            # Si el número de filas introducido por el usuario es 0:
            if (dimension1 == 0):
                # Se rompe el bucle sin que se haya indicado que debe reiniciarse.
                break

            # En caso contrario:
            else:
                # Se devuelve a la variable shouldRestart a su estado anterior para que no afecte al otro bucle.
                shouldRestart = True

            # Se ejecuta otro bucle do-while en el que se pregunta al usuario el número de columnas de las matrices que quiere buscar.
            while (shouldRestart):
                # Limpia la pantalla
                clearScreen ()

                # Se almacena la respuesta del usuario.
                dimension2 = input ('Introduce el número de columnas de la matriz [0 para cancelar]: ')

                # Se intenta convertir la respuesta del usuario a un número entero o flotante.
                try:
                    dimension2 = fracToFloat (dimension2)

                # Se haya podido o no:
                finally:
                    # Si la respuesta del usuario es un número entero que sea mayor o igual que 0:
                    if (type (dimension2) == int and dimension2 >= 0):
                        # No se reinicia el bucle para preguntar al usuario el número de filas.
                        shouldRestart = False

            # Si el número de columnas introducido por el usuario es 0:
            if (dimension2 == 0):
                # Se rompe el bucle sin que se haya indicado que debe reiniciarse.
                break

            # En caso contrario:
            else:
                # Se devuelve a la variable shouldRestart a su estado anterior para que no afecte al otro bucle.
                shouldRestart = True

            # Limpia la pantalla
            clearScreen ()

            # Se crea una lista en la que estarán las matrices cuyas dimensiones coincidan con las que el usuario busca.
            mxnMatrixList = []

            # Se analiza el conjunto de propiedades de cada matriz en la lista de propiedades de las matrices.
            for properties in propertyList:
                # Si la matriz es regular y no tiene incógnitas, es decir, su lista de propiedades tiene más de dos elementos:
                if (len (properties) > 2):
                    # Si el número de filas y el número de columnas (tercer y cuarto elemento de la lista) coinciden con los especificados por el usuario.
                    if (properties [2] == dimension1 and properties [3] == dimension2):
                        # Añade la matriz a la lista de matrices de mxn dimensiones.
                        mxnMatrixList.append (properties [0])

            # Si la longitud de la lista de matrices de mxn dimensiones tiene una longitud de 0:
            if (len (mxnMatrixList) == 0):
                # Es que no hay matrices de mxn dimensiones entre las introducidas por el usuario.
                print (f'No se ha encontrado ninguna matriz de {dimension1}×{dimension2} dimensiones entre las introducidas.')

            # En caso contrario:
            else:
                # Hay al menos una matriz de mxn dimensiones entre las introducidas por el usuario.
                print (f'Se han encontrado {len (mxnMatrixList)} matrices de {dimension1}×{dimension2} dimensiones.')

                # Por cada matriz de mxn dimensiones en la lista:
                for matrix in mxnMatrixList:
                    # Se imprime en pantalla con el estilo 'default'.
                    print ('\n' + matrixToString (prettifyMatrixElements (matrix), 'default'))

            # Sale del modo de muestreo cuando el usuario pulse Enter.
            input ('\n\nPulsa Enter para continuar.')

        # Si el usuario ha elegido mostrar la matriz más grande:
        elif (option == '2'):
            # Limpia la pantalla.
            clearScreen ()

            # Se analiza el conjunto de propiedades de cada matriz en la lista de propiedades de las matrices.
            for properties in range (len (propertyList)):
                # Si la matriz es regular y no tiene incógnitas, es decir, su lista de propiedades tiene más de dos elementos:
                if (len (propertyList [properties]) > 2):
                    # Se comprueba si ya existe una variable que indique el número de elementos de la matriz más grande.
                    try:
                        biggestMatrix

                    # Si no existe:
                    except:
                        # Es que esta es la primera matriz regular sin incógnitas en ser analizada.
                        # Así que se le asigna el número de elementos de la matriz, es decir, el producto de su número de filas por su número de columas.
                        biggestMatrix = propertyList [properties] [2] * propertyList [properties] [3]

                    # Si ya existe:
                    else:
                        # Se almacena el número de elementos de la matriz siendo analizada.
                        nMatrixElements = propertyList [properties] [2] * propertyList [properties] [3]

                        # Si tiene más elementos que la matriz anteriormente considerada más grande:
                        if (biggestMatrix < nMatrixElements):
                            # Este es el número de elementos de la matriz más grande.
                            biggestMatrix = nMatrixElements

            # Se comprueba si la variable biggestMatrix está declarada, es decir, si había alguna matriz regular sin incógnitas.
            try:
                biggestMatrix

            # Si no lo está:
            except:
                # Es que no había matrices regulares sin incógnitas.
                print ('Ninguna de las matrices a analizar era una matriz regular sin incógnitas.')

            # Si lo está:
            else:
                # Se le dice al usuario el número de elementos de aquellas matrices que son más grandes.
                print (f'Las matrices más grandes entre las introducidas son aquellas con {biggestMatrix} elementos.')

                # Se analiza el conjunto de propiedades de cada matriz en la lista de propiedades de las matrices.
                for properties in range (len (propertyList)):
                    # Si la matriz es regular y no tiene incógnitas, es decir, su lista de propiedades tiene más de dos elementos:
                    if (len (propertyList [properties]) > 2):
                        # Si el producto entre el número de filas (tercer elemento de la lista de propiedades)
                        # y el número de columnas (cuarto elemento) de la matriz es igual al número de elementos de la matriz más grande:
                        if (propertyList [properties] [2] * propertyList [properties] [3] == biggestMatrix):
                            # La matriz se imprime en pantalla con el estilo 'default'.
                            print ('\n' + matrixToString (prettifyMatrixElements (propertyList [properties] [0]), 'default'))

            # Sale del modo de muestreo cuando el usuario pulse Enter.
            input ('\n\nPulsa Enter para continuar.')

        # Si el usuario ha elegido calcular la media de los determinantes:
        elif (option == '3'):
            # Limpia la pantalla.
            clearScreen ()

            # Se declara una lista vacía en la que estarán contenidos los determinantes de aquellas matrices que tengan uno, es decir, las matrices cuadradas.
            determinantList = []

            # Se analiza cada matriz en la lista de propiedades de matrices:
            for properties in propertyList:
                # Si la matriz es una matriz cuadrada sin incógnitas:
                if (properties [1] == 0):
                    # Se añade su determinante a la lista de determinantes.
                    determinantList.append (properties [7])

            # Si no hay ningún determinante en la lista de determinantes:
            if (len (determinantList) == 0):
                # Significa que no había ninguna matriz cuadrada sin incógnitas.
                print ('No había matrices cuadradas sin incógnitas, por lo tanto, no había determinantes para calcular la media.')

            # En caso contrario:
            else:
                # Se crea una variable que contendrá el valor de la media de los determinantes.
                determinantAverage = 0

                # Por cada determinante en la lista de determinantes:
                for determinant in determinantList:
                    # Se suma a la media.
                    determinantAverage += determinant

                # Se calcula la media dividiendo la suma de los determinantes entre el número de determinantes (la longitud de la lista de determinantes).
                # Se intenta convertir a entero si se puede.
                determinantAverage = floatToInt (determinantAverage / len (determinantList))

                # Se imprime en pantalla la media de los determinantes.
                print (f'La media de los determinantes es {determinantAverage}.')

            # Sale del modo de muestreo cuando el usuario pulse Enter.
            input ('\n\nPulsa Enter para continuar.')

        # Si el usuario ha elegido no hacer nada más:
        elif (option == ''):
            # No se vuelve a ejecutar el bucle.
            shouldRestart = False

        # Si la opción introducida no es válida, se vuelve al menú.

# Función clearScreen
# Limpia la pantalla usando el comando del sistema 'cls' en Windows y el comando 'clear' en sistemas tipo Unix (GNU/Linux, macOS, BSD...).
def clearScreen ():
    # Si os.name es 'nt', es decir, el sistema operativo en el que se está ejecutando el programa es Microsoft Windows:
    if (os.name == 'nt'):
        # Se ejecuta el comando 'cls' pero asignando su salida a una variable vacía para que no imprima '0'.
        _ = os.system ('cls')

    # Si os.name es 'posix', es decir, el sistema operativo en el que se está ejecutando el programa es de tipo Unix:
    elif (os.name == 'posix'):
        # Se ejecuta el comando 'clear' pero asignando su salida a una variable vacía para que no imprima '0'.
        _ = os.system ('cls')

    # Si es otro tipo de sistema os.name será 'java', pero esta función no da soporte a ese tipo de sistemas.

# Esta parte del código cumple un rol parecido al que cumple la función main en otros lenguajes como C.

# Se obtiene la fecha de ejecución del programa, cuyo formato es el siguiente:
# Año-Mes-Día_Hora_Minuto_Segundo
executionDate = datetime.today ().strftime ('%y-%m-%d_%H-%M-%S')

# Para la versión estándar (versión 0):
if (version == 0):
    # Primero, se comprueba si hay una configuración definida.
    try:
        config

    # Si no la hay:
    except NameError:
        # Crea una configuración vacía.
        config = {}

    # A continuación, se obtiene y testea la configuración.
    # Sí algo no está bien, se sale con el código de error correspondiente.
    # Los errores se generan de forma secuencial, es decir, se leen las opciones según el orden en el que aparecen en la documentación.
    # Por lo tanto, si hay más de una opción mal especificada, se saldrá con el código de error de esa opción
    # y una vez arreglado el error se saldrá con el código de error del siguiente parámetro no válido.
    config = testConfig (config)

# Para la versión Prog (versión 1):
elif (version == 1):
    # Se genera un menú de bienvenida en función del nombre, título, subtítulo y fecha de ejecución del programa.
    print (mainMenu ())

    # Pregunta al usuario en qué modo desea usar el programa.
    mode = input ('Introduce el modo en el que operar (Enter para salir): ')

    # Si el usuario ha introducido un string vacío, es decir, ha pulsado la tecla Enter:
    if (mode == ''):
        # Limpia la pantalla.
        clearScreen ()

        # Sale del programa con el código de error 0, es decir, se sale sin errores.
        sys.exit (0)

    # Intenta convertir el modo introducido por el usuario en un entero.
    try:
        mode = int (mode)

    # Da igual si se ha podido o no:
    finally:
        # Se crea una configuración en la que están contenidas únicamente la opción 'mode' y la opción 'path' con el valor de 'NoInputYet', que permite omitir el testeo.
        config = {
            'mode': mode,
            'path': 'NoInputYet'
        }

        # Se comprueba si el usuario ha introducido una opción válida.
        testConfig (config)

    # Si el usuario no ha salido del programa y la opción 'mode' ha sido bien definida se sigue con el programa.
    # Si no, se habrá salido con el código de error 3.

    # Pregunta al usuario la ruta del archivo.
    path = input ('\nIntroduce la ruta del archivo [Enter para salir]: ')

    # Añade la ruta introducida por el usuario a la configuración como el valor de la opción 'path'.
    config.update ({'path': path})

    # Se testea la configuración.
    # Da igual que se rellene con los valores por defecto del resto de opciones ya que no se van a tener en cuenta en esta versión del programa.
    config = testConfig (config)

    # Si todo ha ido bien, se sigue con el programa.
    # Si no, se habrá salido y avisado al usuario del error.

# Si la versión especificado no es ni 0 ni 1.
else:
    # Genera un mensaje de error y sale con el código de error 2.
    print ('El programa solo tiene las versiones 0 y 1.')
    sys.exit (2)

# Si el programa está en modo 0 (modo matricial):
if (config ['mode'] == 0):
    # Primero,se obtiene la lista de matrices y se genera la lista de propiedades de las respectivas matrices.
    # La lista de matrices se saca del archivo especificado en la opción 'path',
    # de una lista de matrices aleatorias (con las características especificadas en las opciones) o de una única matriz identidad de orden 3.
    matrixList, propertyList = generateMatrixList (config ['path'] + '.input')

    # Luego, se rellena la lista de propiedades de las matrices.
    for matrix in range (len (matrixList)):
        # Por cada matriz, la analiza y rellena su entrada en la lista de propiedades de las matrices.
        propertyList [matrix] = matrixProperties (matrixList [matrix])

    # A continuación, si el programa está en la versión Prog (versión 1):
    if (version == 1):
        # Se ejecuta el menú de opciones, que devuelve los elementos introducidos hayan sido cambiados o no.
        matrixList, propertyList = optionMenu (0, matrixList, propertyList)

    # Luego, se rellena la lista de propiedades de las matrices.
    for matrix in range (len (matrixList)):
        # Por cada matriz, la analiza y rellena su entrada en la lista de propiedades de las matrices.
        propertyList [matrix] = matrixProperties (matrixList [matrix])

    # Por último, se exportan las matrices y sus propiedades al archivo de salida, usando el estilo proporcionado por el usuario.
    # Se escriben en el archivo especificado en la opción 'path'.
    exportMatrixList (propertyList)

    # Como último paso solo si el programa está en la version 1:
    if (version == 1):
        # Se muestra el menú de opciones adicionales de las matrices regulares sin incógnitas.
        matrixOptionMenu (propertyList)

# Si el programa está en modo 1 (modo ecuacional):
else:
    # Primero, se obtiene la lista de sistemas de ecuaciones y se genera la lista de soluciones de los respectivos sistemas de ecuaciones.
    # La lista de sistemas de ecuaciones se saca del archivo especificado en la opción 'path'.
    # En el caso de los sistemas de ecuaciones, esta es la única posibilidad.
    eqSysList, solutionList = parseEquationSystemList (config ['path'] + '.input')

    # A continuación, si el programa está en la versión Prog (versión 1):
    if (version == 1):
        # Se ejecuta el menú de opciones, que devuelve los elementos introducidos hayan sido cambiados o no.
        eqSysList, solutionList = optionMenu (1, eqSysList, solutionList)

    # Luego, se analiza cada sistema de ecuaciones y se resuelve si es compatible determinado.
    # Añade listas con los siguientes elementos en orden a la lista de soluciones de los sistemas de ecuaciones:
    # - El tipo de sistema: incompatible (0), compatible indeterminado (1) o compatible determinado (2)
    # - La lista de incógnitas (en caso de ser compatible determinado).
    # - Cada uno de sus valores (en caso de ser compatible determinado).
    for eqSys in range (len (eqSysList)):
        # Rellena la entrada respectiva de la lista de soluciones (que no deja de ser el análogo del modo ecuacional de la lista de propiedades de matrices)
        # con los elementos mencionados anteriormente.
        solutionList [eqSys] = solveEquationSystem (eqSysList [eqSys])

    # Por último, se escriben los sistemas de ecuaciones y sus propiedades (tipo de sistema y valores de las variables)
    # en el archivo de salida especificado en la opción 'path'.
    exportEquationSystemList (eqSysList, solutionList)

# Antes de salir del programa, se limpia la pantalla.
clearScreen ()