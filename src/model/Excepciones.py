#Excepciones tablas

class ExcepcionCrearTabla(Exception):
    """La tabla ya existe"""

class ExcepcionEliminarTabla(Exception):
    """No hay ninguna tabla que eliminar"""
    pass

class ErrorConsultarArchivo(Exception):
    """El archivo no existe"""
    

class ErrorModificarArchivo(Exception):
    """Ese id no existe"""

class ErrorEliminarArchivo(Exception):
    "El archivo no existe"
    
class ErrorInsertarArchivo(Exception):
    """No se puede ingresar letras en el ID"""
    pass

class ErrorTablaNoExiste(Exception):
    """No hay ninguna tabla"""
    pass

class ErrorNoEncontrado(Exception):
    """El archivo ha sido eliminado"""
    pass