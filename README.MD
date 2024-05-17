# Proyecto Lenguajes de Programación y Código Limpio

## ¿Quién hizo esto?
- **Julio Ochoa**
- **Valeria Solarte**

## ¿Qué es y para qué es?
El proyecto consiste en un conjunto de funciones y pruebas unitarias en Python para la compresión y descompresión de archivos de audio en formatos MP3. Su propósito es proporcionar una herramienta que permita a los usuarios comprimir archivos de audio para ahorrar espacio en disco y descomprimirlos cuando sea necesario.

## ¿Cómo lo hago funcionar?

### Prerrequisitos:
- Python instalado en el sistema.
- Crear una base de datos PostgreSQL y configurar los respectivos datos de acceso.
- Instalar psycopg2 con el comando: `pip install psycopg2`
- Acceso al sistema de archivos donde se encuentren los archivos de audio a comprimir o descomprimir.

### Ejecución:
Para comprimir un archivo de audio, seleccione "comprimir" en la consola y la función `comprimir_audio()` del módulo `logicaComprension` hará la compresión. Debe proporcionar la ruta del archivo original y la ruta donde se guardará el archivo comprimido.

Para descomprimir un archivo de audio, seleccione "descomprimir" en la consola y la función `descomprimir_audio()` del módulo `logicaComprension` hará la descompresión. Debe proporcionar la ruta del archivo comprimido y la ruta donde se guardará el archivo descomprimido.

## ¿Cómo está hecho?
El proyecto está implementado en Python y utiliza el módulo `gzip` para la compresión y descompresión de archivos. La estructura del proyecto incluye:

### Componentes:
- **logicaComprension.py**:
  - Contiene las funciones `comprimir_audio()` y `descomprimir_audio()` para realizar la compresión y descompresión de archivos de audio, respectivamente.
  - Define excepciones personalizadas para manejar errores específicos durante la ejecución.

- **ControladorArchivos.py**:
  - Contiene funciones para interactuar con la base de datos PostgreSQL, gestionando operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para los archivos.
  - Incluye métodos como `CrearTabla()`, `InsertarArchivo()`, `ConsultarArchivo()`, `ModificarArchivo()`, y `EliminarArchivo()` para manejar los datos de los archivos de audio almacenados en la base de datos.
  - Implementa manejo de errores robusto a través de excepciones personalizadas para garantizar que los errores en las operaciones de base de datos sean comunicados claramente al usuario.
  - Utiliza `psycopg2` para la conexión y manipulación de la base de datos, asegurando transacciones seguras y eficientes.


### Pruebas unitarias:
- **Comunicacionestest.py** y **TestMVC.py** 
  - Utilizan el módulo `unittest` de Python para realizar pruebas automatizadas de las funciones de compresión y descompresión.

- **ComunicacionesConsole.py**:
  - Proporciona una interfaz de usuario simple para que los usuarios compriman y descompriman archivos de audio. Utiliza las funciones proporcionadas por el módulo `logicaComprension`.

### Organización de los módulos:
- **src**:
  - Contiene la carpeta `Compress` donde se encuentra el archivo `logicaComprension.py`.
  - Contiene la carpeta `Consola` donde se encuentra el archivo `ComunicacionesConsole.py` y `ConsolaDB.py`.
- **tests**:
  - Contiene el archivo `Comunicacionestest.py`.
  - Contiene el archivo `TestMVC.py`.
## Uso

Para ejecutas la consola , desde la carpeta del programa , use el comando 

 `TrabajoCodigoLimpio>python src/Consola/ComunicacionesConsole.py`

Para ejecutar las pruebas unitarias, desde la carpeta del programa, use el comando.

`TrabajoCodigoLimpio>python tests/Comunicacionestest.py`

Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas


  `import sys` 
  `sys.path.append("src")`



## Database-MVC.

### Requisitos:
Asegúrese de tener una base de datos PostgreSQL y sus respectivos datos de acceso. Modifique el archivo `SecretConfig-Sample.py` a `SecretConfig.py` e ingrese en este archivo los datos de conexión a su base de datos.

Establezca el puerto 5432 que es por defecto.

-PGHOST='xxx'

-PGDATABASE='xxxx'

-PGUSER='xxxxx'

-PGPASSWORD='xxx'

-PGPORT = 'xxx'

### Configuración de la base de datos:
Esta aplicación requiere que esté creada una tabla llamada Archivos. Utilice el script en `sql/archivos.sql` para crearla antes de ejecutar la aplicación.

## Uso en base de datos:
Para ejecutar la consola, desde la carpeta de la base de datos, use el comando:

`TrabajoCodigoLimpio>python src/Consola/ConsolaDB.py`

Para ejecutar las pruebas unitarias, desde la carpeta del programa, use el comando:

`TrabajoCodigoLimpio>python tests/testMVC.py`

Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

`import sys`
`sys.path.append("src")`

Recuerde que el archivo que desee insertar debe existir y no podrá insertar un archivo que no exista. Verifique los archivos guardados localmente.