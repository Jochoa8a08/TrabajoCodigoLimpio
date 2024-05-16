# Proyecto Lenguajes de programacion y codigo limpio

## ¿Quién hizo esto?
Julio Ochoa 
Valeria Solarte

## ¿Qué es y para qué es?

El proyecto consiste en un conjunto de funciones y pruebas unitarias en Python para la compresión y descompresión de archivos de audio en formatos MP3. El propósito es proporcionar una herramienta que permita a los usuarios comprimir archivos de audio para ahorrar espacio en disco y descomprimirlos cuando sea necesario.

## ¿Cómo lo hago funcionar?

- Prerrequisitos:
Python instalado en el sistema.
Crea una base de datos  PostgreSQL y sus respectivos datos de acceso
Instalar psycopg2 con el comando pip install psycopg2
Instalar 
Acceso al sistema de archivos donde se encuentren los archivos de audio a comprimir o descomprimir.

- Ejecución:
Para comprimir un archivo de audio, se debe seleccionar comprimir en la consola  y la función comprimir_audio() del módulo logica hara la comprension. Se debe proporcionar la ruta del archivo original  y la ruta donde se guardará el archivo comprimido.

Para descomprimir un archivo de audio, se debe seleccionar descomprimir en la consola y la función descomprimir_audio() del módulo logica hara la descomprension. Se debe proporcionar la ruta del archivo comprimido y la ruta donde se guardará el archivo descomprimido.
Es importante ejecutar estos comandos desde el entorno de ejecución de Python o desde la línea de comandos del sistema.

## ¿Cómo está hecho?

El proyecto está implementado en Python y utiliza el módulo gzip para la compresión y descompresión de archivos. La estructura del proyecto incluye:

archivo logicaComprension.py:

Contiene las funciones comprimir_audio() y descomprimir_audio() para realizar la compresión y descompresión de archivos de audio, respectivamente.
Define excepciones personalizadas para manejar errores específicos durante la ejecución.

Pruebas unitarias:

archivo Comunicacionestest.py:
Utiliza el módulo unittest de Python para realizar pruebas automatizadas de las funciones de compresión y descompresión.
Se realizan pruebas para casos normales, casos de error y casos excepcionales, validando el comportamiento esperado de las funciones bajo diferentes condiciones.

archivo ComunicacionesConsole.py:
El proposito de este es proporcionar una interfaz de usuario simple para que los usuarios compriman y descompriman archivos de audio. Utiliza las funciones proporcionadas por el módulo logicaComprension para llevar a cabo estas operaciones. El bucle principal permite al usuario realizar múltiples operaciones de compresión y descompresión en una sola ejecución del programa, terminando cuando el usuario elige salir del programa.

organización de los módulos:
carpeta src:
contiene la carpeta Compress donde se encuentra el archivo de logicaComprension.py
contiene la carpeta Consola donde se encuentra el archivo de ComunicacionesConsole.py
carpeta tests:
contine el archivo Comunicaionestest.py

## Uso

Para ejecutas la consola , desde la carpeta del programa , use el comando 

 TrabajoCodigoLimpio>python src/Consola/ComunicacionesConsole.py

Para ejecutar las pruebas unitarias, desde la carpeta del programa, use el comando

`
  TrabajoCodigoLimpio>python tests/Comunicacionestest.py


`
Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

`
  import sys
  sys.path.append("src")
`


# database-mvc

## Requisitos

Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso

En el archivo SecretConfig.py  establezca en este archivo los datos de conexion a su base de datos.

## Configuracion de la base de datos

Esta aplicacion requiere que este creada una tabla llamada Archivos.
Utilice el script en sql\archivos.sql para crear antes de ejecutar la aplicacion

## Uso en base de datos

Para ejecutas la consola , desde la carpeta de la base de datos , use el comando 

`
 TrabajoCodigoLimpio>python src/Consola/ConsolaDB.py

`

Para ejecutar las pruebas unitarias, desde la carpeta del programa, use el comando

`
  TrabajoCodigoLimpio>python tests/testMVC.py
`

Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

`
  import sys
  sys.path.append("src")
`

Recuerde que el archivo que desee insertar debe existir y no podra insertar un archivo que no exista , verifique los archivos guardados localmente.
