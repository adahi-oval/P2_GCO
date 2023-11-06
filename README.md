# Sistemas de recomendación - Modelos basados en el contenido.

## Instrucciones

## Descripción del código

En primer lugar, todo lo necesario para el funcionamiento del programa se lee de los documentos pasados por el usuario. Para ello se utiliza un módulo creado por nosotros llamado `docReader`. En este módulo se encuentran 4 funciones en total. 

Las dos primeras funciones, `readDocs` y `readLema` se utilizan para formar las listas en `Python` que utilizaremos a lo largo del programa. La función `readDocs` lee el fichero con los documentos y crea una lista con ellos, también se utiliza para leer la lista de ***stop words*** para crear una lista con ellas. La función `readLema` lee el documento con el cual se crea una lista de tuplas de dos elementos, aprovechando el formato similar al de un diccionario **`JSON`**.

Las dos funciones restantes, `clearStopWords` y `lematizacion` se encargan de formatear los documentos para su posterior análisis.

La primera, `clearStopWords` se encarga de separar el documento proporcionado en una lista de palabras. Esta lista la recorre para encontrar las palabras que no coinciden con las ***stop words*** y juntarlas de nuevo en un documento limpio de ellas.

La segunda, `lematizacion` es similar a la primera, pero esta recorre la lista de palabras buscando las que coindicen con los primeros elementos en la lista de tuplas para sustituirlas por el segundo elemento. 