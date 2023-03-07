## Description

    ACTIVIDAD LECCIÓN 1

        Ejecutando el fichero finanzas.py realizamos las tareas que se piden en el ejercicio de 
        la actividad 1 de BPP.

        Primeramente leemos el archivo finanzas2020.csv, comprobando que existe, que se lee correctamente y 
        que tiene 12 columnas.

        Posteriiormente depuramos los datos, para trasnformar los datos a float y limpiar cualquier erro que pudiera haber,
        tanto falta de datos como datos de tipo no numérico.

        Una vez con los datos correctos descargados en dataframe, se realizan los cáculos que se piden en el enunciado.
        y se visualiza la gráfica.
    
    ACTIVIDAD LECCIÓN 2

        He basado la práctica de la actividad 2 en hacer pruebas de la práctica de la actividad 1.

        PYTEST:

            Ejecutando pytest tanto desde el directorio principal como desde el directorio test,
            se ejecutará la batería de test del archivo test_actividad1.py.

            En ese fichero se especifica y está explicado cada prueba que se realiza.

            En la documentación de pytest, 

            https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html

            sugiere como buena práctica, poner los test en directorios a parte, que bien puede ser dentro de la estructura del programa 
            o totalmente independiente.

            En mi caso está dentro de la estructura, pero me encintré con el problema de la importación de los archivos

            que resolví en este caso creando los archivos __init__.py, con esto no da problemas de importación.

        UNNITEST

            Para el caso de Unnitest, tuve que nombrarlo con algo diferente a test, para juntar en el mismo ejercico
            la práctica de pytest y unnitest sin que se interfieran.

            Para ejecutar los test, se hará ejecuntado el archivo pruebas_unittest.py, 
            en el código comnetado se explican todas las pruebas realizadas.

            También tuve el problema de la importación de los archivos, que en este caso no me valía la solución anterior, 
            sino que tuve que hacer uso de lo siguiente:

                import sys
                import os
                # get current directory
                path = os.getcwd()
                # parent directory
                parent = os.path.dirname(path)
                # appending a path
                sys.path.append(parent)
            
            Con esto, y al ener que ejecutar la prueba desde el directorio de test, 
            agragamos al sys.path la direccion de busqueda del archivo principal,
            cosa que con pytest no me valía ya que ejecutamos pytest, desde cualquier direcorio del 
            programa y no obligados desde test.

    ACTIVIDAD LECCIÓN 3

        He basado la práctica de la actividad 3 en la práctica de la lección 1 y 2.
 
        He realizado la documentación de dicha actividad en formato HTML

        He modificado ligeramente los menús para un aspecto más legible y he añadido una imagen a modo de prueba.

        Todo ello realizado con sphinx



## DATA SET:

    finanzas2020.csv

## Specifications

    Requirements.txt



