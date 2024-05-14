#ControladorArchivos.py
import sys
sys.path.append( "src" )
sys.path.append( "." )

import psycopg2

from model.Archivo import Archivo
import SecretConfig

tabla = """CREATE TABLE Archivos (id SERIAL PRIMARY KEY,nombre TEXT NOT NULL,extension TEXT NOT NULL,tamaño INTEGER, fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP); """
class ControladorArchivos:

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute(tabla)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorArchivos.ObtenerCursor()

        cursor.execute("""drop table Archivos""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()
    
    def BuscarArchivoid( cedula ):
        """ Trae un Archivo de la tabla de Archivos por el id """
        cursor = ControladorArchivos.ObtenerCursor()

        cursor.execute("""select id, nombre, extension, tamaño, fecha_creacion from archivos where id = '1010' """)
        
        fila = cursor.fetchone()
        resultado = Archivo( id=fila[0], nombre=fila[1], extension=fila[2], tamaño=fila[3],fecha_creacion=fila[4] )
        return resultado

    #INSERTAR
    def InsertarArchivo( archivo : Archivo ):
        """ Recibe un a instancia de la clase Archivo y la inserta en la tabla respectiva"""
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute( f"""insert into Archivos (id, nombre, extension,tamaño)
                        values ('{archivo.id}', '{archivo.nombre}', '{archivo.extension}',  
                            '{archivo.tamaño}') """ )

        cursor.connection.commit()
    
    #ACTUALIZAR
    def ModificarArchivo(id, nombre=None, extension=None, tamaño=None):
        cursor = ControladorArchivos.ObtenerCursor()
        updates = []
        params = []
        if nombre:
            updates.append("nombre = %s")
            params.append(nombre)
        if extension:
            updates.append("extension = %s")
            params.append(extension)
        if tamaño:
            updates.append("tamaño = %s")
            params.append(tamaño)
        

        set_clause = ", ".join(updates)
        params.append(id)
        cursor.execute(f"""
            UPDATE Archivos
            SET {set_clause}
            WHERE id = %s;
        """, tuple(params))
        cursor.connection.commit()

    #ELIMINAR
    def EliminarArchivo(id):
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute("DELETE FROM Archivos WHERE id = %s;", (id,))
        cursor.connection.commit()
 
    #CONSULTAR
    def ConsultarArchivo(id):
        cursor = ControladorArchivos.ObtenerCursor()
        cursor.execute("SELECT id, nombre, extension, tamaño, fecha_creacion FROM Archivos WHERE id = %s;", (id,))
        fila = cursor.fetchone()
        if fila:
            return Archivo(id=fila[0], nombre=fila[1], extension=fila[2], tamaño=fila[3], fecha_creacion=fila[4])
        return None

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor
