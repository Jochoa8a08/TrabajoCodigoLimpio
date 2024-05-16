#ControladorArchivos.py
"""
    Pertenece a la capa de Acceso a Datos

    Controla las operaciones de almacenamiento de la clase Archivo
"""
import psycopg2
import sys
import os
sys.path.append( "src" )
sys.path.append( "." )

from model.Archivo import Archivo
from model.Excepciones import ExcepcionCrearTabla , ExcepcionEliminarTabla, ErrorModificarArchivo, ErrorInsertarArchivo, ErrorConsultarArchivo, ErrorModificar
import SecretConfig

tabla = """CREATE TABLE Archivos (id SERIAL PRIMARY KEY,nombre TEXT NOT NULL,extension TEXT NOT NULL,tamaño INTEGER, fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP); """
class ControladorArchivos:

    def CrearTabla():
        """Crea la tabla de Archivos en la BD"""
        cursor = ControladorArchivos.ObtenerCursor()
        try:
            cursor.execute("SELECT 1 FROM information_schema.tables WHERE table_name=%s", ('archivos',))
            if cursor.fetchone():
                raise ExcepcionCrearTabla("La tabla ya existe")
            cursor.execute(tabla)
            cursor.connection.commit()
            print("Tabla creada exitosamente.")
        except ExcepcionCrearTabla as e:
            print(e)
        finally:
            cursor.close()

    def EliminarTabla():
        """Borra la tabla de Archivos de la BD"""
        cursor = ControladorArchivos.ObtenerCursor()
        try:
            cursor.execute("SELECT 1 FROM information_schema.tables WHERE table_name=%s", ('archivos',))
            if not cursor.fetchone():
                raise ExcepcionEliminarTabla("No hay ninguna tabla que eliminar")
            cursor.execute("DROP TABLE Archivos")
            cursor.connection.commit()
            print("Tabla eliminada exitosamente.")
        except ExcepcionEliminarTabla as e:
            print(e)
        finally:
            cursor.close()

    def BorrarFilas():
        """ Borra todas las filas de la tabla Archivos (DELETE)"""
        sql = "DELETE FROM Archivos;"
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute(sql)
        cursor.connection.commit()
        cursor.close()
    

    #INSERTAR
    def InsertarArchivo( archivo : Archivo ):
        """ Recibe un a instancia de la clase Archivo y la inserta en la tabla respectiva"""
        if not str(archivo.id).isdigit():
            raise ErrorInsertarArchivo("El ID debe ser un número.")
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute( f"""insert into Archivos (id, nombre, extension,tamaño)
                        values ('{archivo.id}', '{archivo.nombre}', '{archivo.extension}',  
                            '{archivo.tamaño}') """ )
        cursor.connection.commit()
        cursor.close()

    #CONSULTAR
    def ConsultarArchivo(id):
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute("SELECT id, nombre, extension, tamaño, fecha_creacion FROM Archivos WHERE id = %s;", (id,))
        fila = cursor.fetchone()
        if fila:
            return Archivo(id=fila[0], nombre=fila[1], extension=fila[2], tamaño=fila[3], fecha_creacion=fila[4])
        else:
            if not os.path.exists(id):
                 raise ErrorConsultarArchivo(f"No se encontró el archivo con id {id}.")
    
    
    
    #Modificar
    def ModificarArchivo(id, nombre=None, extension=None):
        cursor = ControladorArchivos.ObtenerCursor()

        # Verificar si el archivo con el ID proporcionado existe
        cursor.execute("SELECT 1 FROM Archivos WHERE id = %s;", (id,))
        if not cursor.fetchone():
            cursor.close()
            raise ErrorModificarArchivo("Ese id no existe, intente de nuevo")
        
        if nombre is None and extension is None:
            cursor.close()
            raise ErrorModificar("No se puede modificar el ID del archivo")

        updates = []
        params = []
        if nombre:
            updates.append("nombre = %s")
            params.append(nombre)
        if extension:
            updates.append("extension = %s")
            params.append(extension)
        
        set_clause = ", ".join(updates)
        params.append(id)
        cursor.execute(f"""
            UPDATE Archivos
            SET {set_clause}
            WHERE id = %s;
        """, tuple(params))
        cursor.connection.commit()
        cursor.close()
    

    #ELIMINAR
    def EliminarArchivo(id):
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute("DELETE FROM Archivos WHERE id = %s RETURNING id;", (id,))
        cursor.connection.commit()
        cursor.close()


    def ConsultarTodosLosIds():
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute("SELECT id FROM Archivos;")
        ids = cursor.fetchall()
        cursor.close()
        return [id[0] for id in ids]

    def solicitar_id():
        while True:
            id = input("Ingrese el id del archivo (solo números): ")
            if id.isdigit():
                return id
            print("El ID debe ser un número. Intente de nuevo con un ID diferente.")
    
    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor
