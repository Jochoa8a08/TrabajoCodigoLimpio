from datetime import date

class Archivo:
    """"
    Representa a un archivo  en la aplicación

    """
    def __init__( self, id,nombre, extension, tamaño, fecha_creacion )  :
        self.id = id
        self.nombre = nombre
        self.extension = extension
        self.tamaño = tamaño
        self.fecha_creacion = fecha_creacion


    def esIgual( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Archivo
        
        """
        assert( self.id == comparar_con.id )
        assert( self.nombre == comparar_con.nombre )
        assert( self.extension== comparar_con.extension )
        assert( self.tamaño== comparar_con.tamaño )
        assert( self.fecha_creacion== comparar_con.fecha_creacion )

