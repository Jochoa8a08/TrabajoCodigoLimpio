#Excepciones tablas

class ExcepcionCrearTabla(Exception):
    """La tabla ya existe"""

class ExcepcionEliminarTabla(Exception):
    """No hay ninguna tabla que eliminar"""
    pass

class ErrorConsultarArchivo(Exception):
    """El archivo no existe"""
    pass

class ErrorModificarArchivo(Exception):
    """Ese id no existe intente de nuevo"""

class ErrorModificar(Exception):
    """No puedes modificar el ID"""
    
class ErrorInsertarArchivo(Exception):
    """No se puede ingresar letras en el ID"""
    pass

class ErrorTablaNoExiste(Exception):
    """No hay ninguna tabla"""
    pass

class ErrorNoEncontrado(Exception):
    """El archivo ha sido eliminado"""
    pass