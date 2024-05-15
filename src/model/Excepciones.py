#Excepciones tablas

class ExcepcionCrearTabla(Exception):
    """La tabla ya existe"""

class ExcepcionEliminarTabla(Exception):
    """No hay ninguna tabla que eliminar"""
    pass

class ErrorInsertarArchivo(Exception):
    """El archivo no existe"""

class ErrorModificarArchivo(Exception):
    """Ese id no existe intente de nuevo"""

class ErrorTablaNoExiste(Exception):
    "No hay ninguna tabla"
    pass